from django.db import models

# Create your models here.
class Id(models.Model):
    std_name= models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.std_name

class father_name(models.Model):
    std_id= models.ForeignKey(Id,on_delete=models.PROTECT)
    fatherN = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.fatherN

class adm_date(models.Model):
    name=models.ForeignKey(father_name,on_delete=models.PROTECT)
    date= models.DateField()

    def __str__(self):
        return str(self.date)
