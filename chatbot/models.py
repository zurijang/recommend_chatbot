from django.db import models
# DB table


class AddressData(models.Model):
    objects = models.Manager()
    region = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    search_name = models.CharField(max_length=40)
    rank = models.FloatField()
    search_count = models.IntegerField()
    link = models.CharField(max_length=50)
    month = models.IntegerField()
    year = models.IntegerField()
    season = models.CharField(max_length=5)
    postnum = models.IntegerField()
    search_type = models.CharField(max_length=50)
    search_name2 = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    latitud = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    score = models.FloatField()
# localhost:8000/admin
# python manage.py createuseruser   : admin 계정 생성

class AlgorithmData(models.Model):
    objects = models.Manager()
    search_name = models.CharField(max_length=40)
    search_type = models.CharField(max_length=50)
    search_count = models.IntegerField()
    postnum = models.IntegerField()
    YMD = models.CharField(max_length=8)
    rank = models.IntegerField()