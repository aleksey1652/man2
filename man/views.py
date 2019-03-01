from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from man.models import mservice,otpr,dapis,bar

def logi(request):
    #return HttpResponse("Hello, world. You're at the man index.")    
    #global Q    
    #m=Q       
    #n=m+10
    #Q=n
    mservice_list=mservice.objects.order_by('lo')
    #if len(otpr_list)<m:
    #   m=0
    #    n=m+10
    #   Q=n
    #otpr_list=otpr.objects.order_by('na')#[m:n]    
    #template = loader.get_template('ma/ma_sender.html')
    context = {
        'mservice_list': mservice_list,
    }
    return render(request, 'man/logi.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the ma ma_sender.")

def man_sender(request,mservice_id):
    #return HttpResponse("Hello, world. You're at the man_sender.")    
    otpr_list=otpr.objects.filter(mservice__id=mservice_id)
    context = {
        'otpr_list': otpr_list,
    }
    return render(request, 'man/man_sender.html', context)

def detail(request,otpr_id):
    #return HttpResponse("Hello, world. You're at the detail.")
    otpr_list = get_object_or_404(otpr, pk=otpr_id)
    return render(request, 'man/detail.html', {'oko': otpr_list})

def barr(request, otpr_id):
    
    
    oo=get_object_or_404(bar, pk=otpr_id)
    return render(request, 'man/bar.html', {'oo': oo})
    #return HttpResponse("Hello %s " % otpr_id )

def fill(request, otpr_id):
    f=get_object_or_404(bar, pk=otpr_id)
    return render(request, 'man/fill.html', {'f': f})

def htm(request, otpr_id):
    f=bar.objects.get(id=otpr_id)
    return HttpResponse(f.htmlt1)
    #return HttpResponse('deko')
