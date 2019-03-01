from django.db import models


class mservice(models.Model):
    lo=models.CharField(max_length=500,unique=True,default='ukr_net')

    def __str__(self):
        return self.lo
    
class otpr(models.Model):
    na=models.CharField(max_length=100)
    mservice=models.ManyToManyField(mservice)

    def __str__(self):
        return self.na

class dapis(models.Model):
    da=models.DateField(unique=True)
    otpr = models.ManyToManyField(otpr, through='bar')

    def __str__(self):
        return self.da.strftime('%Y,%m,%d')

class bar(models.Model):
    nu=models.IntegerField()
    nu2=str(nu)    
    seen=models.BooleanField(default=True)
    text=models.TextField()
    subj=models.CharField(max_length=500)
    htmlt1=models.TextField()
    htmlt2=models.TextField()
    fmail=models.CharField(max_length=500,default=' ')
    dapis = models.ForeignKey(dapis, on_delete=models.CASCADE)
    otpr = models.ForeignKey(otpr, on_delete=models.CASCADE)
    #mservice = models.ForeignKey(mservice, on_delete=models.CASCADE)

    def __str__(self):
        return self.nu2

