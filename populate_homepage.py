import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','preschool.settings')

import django
django.setup()

import random
from homepage.models import Id,father_name,adm_date

from faker import Faker

fakegen =Faker()

def populate(N=5):

    for entry in range(N):
        fake_id = fakegen.name()
        fake_father= fakegen.name()
        fake_date= fakegen.date()

        sName=father_name.objects.get_or_create(std_id=fake_id,fatherN=fake_father)[0]

        admDate= adm_date.objects.get_or_create(name=sName,date=fake_date)[0]


if __name__ =='__main__':

    populate(6)
