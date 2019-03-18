from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import NameForm
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
    mservice_list=mservice.objects.get(id=mservice_id)
    ch_list=[(0,'Поиск по отправителю'),(1,'Поиск по теме письма'),(2,'Поиск внутри письма')]
    context = {
        'otpr_list': otpr_list,
        'm':mservice_list,
        'ch_list':ch_list,
    }
    return render(request, 'man/man_sender2.html', context)

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

def your_name(request,che,m):
    #form = NameForm(request.POST)
    m2=mservice.objects.get(id=m)
    ch_list=[(0,'Поиск по отправителю'),(1,'Поиск по теме письма'),(2,'Поиск внутри письма')]
    man_otpr_list=otpr.objects.filter(mservice__id=m)
    context = {
                'otpr_list': man_otpr_list,
                'm':m2,
                'ch_list':ch_list,
    }
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            subject = form.cleaned_data['your_name']
            ch_list=[(0,'Поиск по отправителю'),(1,'Поиск по теме письма'),(2,'Поиск внутри письма')]
            man_otpr_list=otpr.objects.filter(na__icontains=subject,mservice__id=m)
            #man_otpr_list=otpr.objects.filter(bar__subj__icontains=subject,mservice__id=m)
            if int(che) == 1:
                b=bar.objects.filter(subj=subject)
                if b.count() != 0:
                    return render(request, 'man/bar.html', {'oo': b[0]})
            if int(che) == 2:
                b=bar.objects.filter(text=subject)
                if b.count() != 0:
                    return render(request, 'man/bar.html', {'oo': b[0]})
            #b=bar.objects.get(subj=subject)
            #return HttpResponse(b.nu)
            #man_otpr_list=otpr.objects.filter(bar__text__icontains=subject,mservice__id=m)
            context = {
                'otpr_list': man_otpr_list,
                'm':m2,
                'ch_list':ch_list,
            }
            return render(request, 'man/man_sender2.html', context)
            #return HttpResponse("Hello %s " % subject )            
            #return HttpResponseRedirect('/your-name/')
            
    # if a GET (or any other method) we'll create a blank form
    else:
        #form = NameForm()
        
        context = {
                'otpr_list': man_otpr_list,
                'm':m2,
                'ch_list':ch_list,
        }
    return render(request, 'man/man_sender2.html', context)
    #return render(request, 'man/man_sender.html', {'form': form,'m':m2})
    #return HttpResponse("Hello  %s " % form)

def radio(request,m):
    #return HttpResponse("Hello %s " % m )
    m2=mservice.objects.get(id=m)
    otpr_list=otpr.objects.filter(mservice__id=m)
    try:        
        subject=request.POST['ch']        
        context = {
            'ch': subject,
            'm':m2,
            'otpr_list': otpr_list,        
        }
    except :
        return HttpResponse("Выберите что-то")
        
    return render(request, 'man/man_sender.html', context)
    

