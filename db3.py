from ma.models import otpr,dapis,bar
from datetime import date
def dbfill3(hh1):
    htmlt2=''
    #for x in hh1[4]:
    #    htmlt1=htmlt1+' '+x
    for x in hh1[5]:
        htmlt2=htmlt2+' '+x
    if otpr.objects.filter(na=hh1[2]).count()==0:
        a=otpr.objects.create(na=hh1[2])
    else:
        a=otpr.objects.get(na=hh1[2])
    if  dapis.objects.filter(da=date(hh1[0][0],hh1[0][1],hh1[0][2])).count()==0:
        b=dapis.objects.create(da=date(hh1[0][0],hh1[0][1],hh1[0][2]))
    else:
        b=dapis.objects.get(da=date(hh1[0][0],hh1[0][1],hh1[0][2]))
    if bar.objects.filter(nu=hh1[6]).count()==0:
        c=bar(otpr=a,dapis=b,nu=hh1[6],text=hh1[3],subj=hh1[1],htmlt1=hh1[4],htmlt2=htmlt2)    
        c.save()
    
