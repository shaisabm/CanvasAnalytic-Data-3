from django.db import models

# Create your models here.

class SampleData(models.Model):
    feature1 = models.CharField(max_length=100, default='sampleData')
    feature2 = models.CharField(max_length=100, default='sampleData')
    feature3 = models.CharField(max_length=100, default='sampleData')
    feature4 = models.CharField(max_length=100, default='sampleData')
    feature5 = models.CharField(max_length=100, default='sampleData')
    feature6 = models.CharField(max_length=100, default='sampleData')
    feature7 = models.CharField(max_length=100, default='sampleData')
    feature8 = models.CharField(max_length=100, default='sampleData')
    feature9 = models.CharField(max_length=100, default='sampleData')
    feature10 = models.CharField(max_length=100, default='sampleData')


