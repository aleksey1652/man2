from man.models import otpr,dapis,bar,mservice
from datetime import date
def dbfilln(hh1,u):
    htmlt2=''
    #for x in hh1[4]:
    #    htmlt1=htmlt1+' '+x
    if hh1[5]:
        for x in hh1[5]:
            htmlt2=htmlt2+' '+x
    else:
        htmlt2=''
    if mservice.objects.filter(lo=u).count()==0:
        l=mservice(lo=u)
        l.save()
    else:
        l=mservice.objects.get(lo=u)
        
    if l.otpr_set.filter(na=hh1[2]).count()==0:
        a=l.otpr_set.create(na=hh1[2])
    else:
        a=l.otpr_set.get(na=hh1[2])
    if  dapis.objects.filter(da=date(hh1[0][0],hh1[0][1],hh1[0][2])).count()==0:
        b=dapis.objects.create(da=date(hh1[0][0],hh1[0][1],hh1[0][2]))
    else:
        b=dapis.objects.get(da=date(hh1[0][0],hh1[0][1],hh1[0][2]))
    if bar.objects.filter(nu=hh1[6]).count()==0:
        c=bar(otpr=a,dapis=b,nu=hh1[6],text=hh1[3],subj=hh1[1],htmlt1=hh1[4],htmlt2=htmlt2)    
        c.save()
