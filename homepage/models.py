from django.db import models

# Create your models here.
class Parent(models.Model):
    parent_id= models.AutoField(primary_key=True)
    parent_fn=models.CharField("Parent First Name",max_length=20)
    parent_ln=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    profession=models.CharField(max_length=30)

    def __str__(self):
        return self.parent_fn

class Grades(models.Model):

    grade_choice_list=(
    ('NUR','Nursery'),
    ('PG','Play Group'),
    ('LKG','Lower KinderGarten'),
    ('UKG','Upper KinderGarten'),
    )
    child_relationship=models.ManyToManyField(Parent,through='Child')
    years_in_school=models.CharField(max_length=20,choices=grade_choice_list,default='NUR')

class Child(models.Model):
    child_parent= models.ForeignKey(Parent, on_delete=models.CASCADE)
    grade=models.ForeignKey(Grades,on_delete=models.CASCADE)
    child_id= models.AutoField(primary_key=True)
    child_name=models.CharField(max_length=30)
    age=models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.child_name


    # def is_senior(self):
    #
    #     return self.years_in_school in (self.LOWERKG,self.UPPERKG)
