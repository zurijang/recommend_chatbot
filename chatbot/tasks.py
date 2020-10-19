import pandas as pd
import numpy as np
import django
import json
from .models import AlgorithmData, AddressData

new_data = AlgorithmData.objects.all()\
    .values('search_name', 'search_type', 'search_count', 'postnum', 'YMD', 'rank')

matrix = pd.DataFrame.from_records(new_data).pivot_table(index='YMD', columns='search_name', values='rank')

TYPE_WEIGHT = 0.1
def pearsonR(s1, s2):
    s1_c = s1-s1.mean()
    s2_c = s2-s2.mean()
    return np.sum(s1_c*s2_c) / np.sqrt(np.sum(s1_c**2)*np.sum(s2_c**2))

def recommend(input_place, matrix=matrix, similar_type = True, reverse=True):
    input_types = new_data.filter(search_name='당진시 왜목마을').values('search_type')[0]['search_type']
    
    result = []
    for place in matrix.columns:
        if place == input_place:
            continue
        
        #rating comparison
        cor = pearsonR(matrix[input_place], matrix[place])
        
        #type comparison
        if similar_type and len(input_types) > 0:
            temp_types = new_data.filter(search_name=place).values('search_type')[0]['search_type']
            
            same_count = np.sum(np.isin(input_types, temp_types))
            cor += (TYPE_WEIGHT*same_count)
            
        if np.isnan(cor):
            continue
        else:
            result.append((place, '{:.6f}'.format(cor), temp_types))
        
    df_result = pd.DataFrame(result, columns = ['상세 검색지명', '상관계수','유형'])
    real_result = df_result[df_result['상관계수'].astype(float).le(0)].sample(n=5)
    return real_result

def input_validation(input_place):
    return new_data.filter(search_name=input_place).count()

def extract_text(recommend_list):
    text_list = []
    for name in (recommend_list['상세 검색지명'].values):
        text_list.append(AddressData.objects.all()\
            .filter(search_name2=name)\
            .values('search_name2', 'link', 'latitud', 'longitude')) 

    text = ''
    for row in text_list:
        row_dict = row.values('search_name2', 'link')[0]
        text += '지명 : ' + row_dict['search_name2'] + '\n지도보기 : ' + row_dict['link'].replace(' ','%20') + '\n\n'
        
    return text