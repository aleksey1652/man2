#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()
from ma.models import otpr,dapis,bar
from datetime import date
b=dapis.objects.all()

for x in b:
    x.otpr.clear()
c=bar.objects.all()

if bar.objects.all().count()==0:
    for x in b:
        x.delete()

a=otpr.objects.all()

for x in a:
    x.delete()

print('dapis=',dapis.objects.all())
print('bar=',bar.objects.all())
print('otpr=',otpr.objects.all())    
