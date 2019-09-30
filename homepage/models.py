from django.db import models

# Create your models here.
class Parent(models.Model):
    Paent_id= models.IntegerField(primary_key=True)
    parent_fn=models.CharField(max_length=20)
    parent_ln=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    profession=models.CharField(max_length=30)

    def __str__(self):
        return self.parent_fn

class Child(models.Model):
    child_parent= models.ForeignKey(Parent, on_delete=models.CASCADE)
    child_id= models.IntegerField(primary_key=True)
    child_name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    grade=models.CharField(max_length=10)

    def __str__(self):
        return self.child_name
