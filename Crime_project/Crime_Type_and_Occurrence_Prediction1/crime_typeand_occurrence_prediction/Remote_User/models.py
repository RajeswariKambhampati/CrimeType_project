from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Crime_details(models.Model):


    INCIDENT_NUMBER= models.CharField(max_length=300)
    OFFENSE_CODE= models.CharField(max_length=300)
    OFFENSE_CODE_GROUP= models.CharField(max_length=300)
    OFFENSE_DESCRIPTION= models.CharField(max_length=300)
    DISTRICT= models.CharField(max_length=300)
    REPORTING_AREA= models.CharField(max_length=300)
    OCCURRED_ON_DATE= models.CharField(max_length=300)
    YEAR= models.CharField(max_length=300)
    MONTH= models.CharField(max_length=300)
    DAY_OF_WEEK= models.CharField(max_length=300)
    Hour= models.CharField(max_length=300)
    UCR_PART= models.CharField(max_length=300)
    STREET= models.CharField(max_length=300)
    Lat= models.CharField(max_length=300)
    Long1= models.CharField(max_length=300)
    Location= models.CharField(max_length=300)


class Crime_type(models.Model):

    INCIDENT_NUMBER = models.CharField(max_length=300)
    OFFENSE_CODE = models.CharField(max_length=300)
    OFFENSE_CODE_GROUP = models.CharField(max_length=300)
    OFFENSE_DESCRIPTION = models.CharField(max_length=300)
    DISTRICT = models.CharField(max_length=300)
    REPORTING_AREA = models.CharField(max_length=300)
    OCCURRED_ON_DATE = models.CharField(max_length=300)
    YEAR = models.CharField(max_length=300)
    MONTH = models.CharField(max_length=300)
    DAY_OF_WEEK = models.CharField(max_length=300)
    Hour = models.CharField(max_length=300)
    UCR_PART = models.CharField(max_length=300)
    STREET = models.CharField(max_length=300)
    Lat = models.CharField(max_length=300)
    Long1 = models.CharField(max_length=300)
    Location = models.CharField(max_length=300)
    CTYPE= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



