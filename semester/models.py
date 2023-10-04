from django.db import models

class Semester(models.Model):
    semestername = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()