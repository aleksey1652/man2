#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()
import imaplib,getpass,email,re,datetime
from email.header import decode_header
import re
d1,d2,d3,get,tex,tex2,tex21,tex22,subl,subl2=0,0,0,0,0,0,[],[],[],[]
def URL_transition(s):
    import webbrowser
    webbrowser.open(s)

def Search_from_subject(s,get,mar):
    global subl    
    count=0
    _,data=get.search(None,'ALL')
    st=data[0].split()
    N=int(input('Сколько последних писем в поиске:'))
    print('Номера писем:')
    strev=st[-N:]
    for x in strev:
        _,data=get.fetch(x,"(BODY.PEEK[HEADER])")
        msg=email.message_from_bytes(data[0][1])
        stext=DEcode_header(msg[mar])        
        if re.findall(r'.*{}.*'.format(s),stext):    
            #print(int(x),end=' ')
            subl.append(int(x))           
            count=count+1                    
    #print(subl)                                    
    if count==0:
       subl.append('нету') #print('нету')
        
def Search_unseen(b,get):
    global subl #,subl2
    _,data=get.search(None,'(UNSEEN)')
    st=data[0].split()
    strev=st[-int(b):]
    print('Номера писем:')
    for x in strev:
        subl.append(int(x))#print(int(x),end=' ')
    #subl2=[x for x in range(1,int(b)+1) if x not in subl]    
    #print()
        
def Search_from(s,get):
    global subl
    _,data=get.search(None,'(FROM "{}")'.format(s))
    st=data[0].split()
    print('Номера писем:')
    for x in st:
        subl.append(int(x))#print(int(x),end=' ')
    #print()

def Search_timedelta(s,get):
    global subl
    date= (datetime.date.today()-datetime.timedelta(int(s))).strftime("%d-%b-%Y")
    print('Номера писем:')
    st=get.search( None, '(SENTSINCE {date})'.format(date=date))[1][0].split()
    for x in st:
        subl.append(int(x))#print(int(x),end=' ')
    #print()  
    
def Search_data(s,get):
    global subl
    spl=s.split('-')
    spl=[int(x) for x in spl]
    s1,s2,s3=spl
    s=datetime.date(s1,s2,s3).strftime("%d-%b-%Y")
    date= (datetime.date(s1,s2,s3)+datetime.timedelta(1)).strftime("%d-%b-%Y")
    print('Номера писем:')
    subl=get.search( None, '(SINCE {} BEFORE {})'.format(s,date))[1][0].split()
    subl=[int(x) for x in subl]
    
def Search_text(s,get):
    global subl
    count=0
    _,data=get.search(None,'ALL')
    st=data[0].split()
    N=int(input('Сколько последних писем в поиске:'))
    strev=st[-N:]
    for x in strev:
        _,data=get.fetch(x,"(BODY.PEEK[])")
        msg=email.message_from_bytes(data[0][1])
        for xi in msg.walk():
            if xi.get_content_type()=="multipart":
                continue
            elif xi.get_content_type()=="text/plain":
                stext= xi.get_payload(decode = True).decode('utf-8')
                #if re.findall(r'\b{}\b'.format(s),stext):
                if re.findall(r'.*{}.*'.format(s),stext):    
                    subl.append(int(x))#print(int(x),end=' ')
                    count=count+1
    #print()                                    
    if count==0:
        subl.append(int('нету'))#print('нету')            
                        
def DEcode_header(ob):
    if ob:
        ob=(re.findall(r'.+',ob))[0]
        
        header_parts = decode_header(ob)        
        res = []
        for decoded_string, encoding in header_parts:
            if encoding:
                decoded_string = decoded_string.decode(encoding)
            elif isinstance(decoded_string, bytes):                
                decoded_string = decoded_string.decode("ascii")                
            res.append(decoded_string)
        return "".join(res)

    return 'нету'   

def GetMailNum2(a,get):
    global d1,d2,d3,texspl,tex2,tex21,tex22
    
    num_mail=bytes(str(a),'utf-8')
    _,data=get.fetch(num_mail,"(BODY.PEEK[])")
    msg=email.message_from_bytes(data[0][1])    
    
    
    for x in msg.walk():        
        if x.get_content_type()=="multipart":
            continue
        elif x.get_content_type()=="text/plain":            
            
            tex=x.get_payload(decode = True).decode('utf-8')
            texspl=tex.split()
            tex=''
            for x in texspl:
                tex=tex+' '+x
                
        elif x.get_content_type()=="text/html":
            
            N=1000 #int(input('html-текст Сколько знаков вывести? : '))
            
            tex2=x.get_payload(decode = True).decode('utf-8')[:N]
            
            for x in re.findall(r'<a.+href="(https://.{40})',tex2):
                tex21.append(x)
                
            
            for x in re.findall(r'<img.+src="(.{80})',tex2):
                tex22.append(x)
                    
        elif x.get_content_maintype()=="image":
            if x.get_content_maintype() != 'multipart' and x.get('Content-Disposition') is not None:
                open('/home/aleksey' + '/' + DEcode_header(x.get_filename()), 'wb').write(x.get_payload(decode='utf-8'))
        elif x.get_content_maintype() != 'multipart' and x.get('Content-Disposition') is not None:
            open('/home/aleksey' + '/' + DEcode_header(x.get_filename()), 'wb').write(x.get_payload(decode='utf-8'))
            
    return msg['DATE'][:17],DEcode_header(msg['Subject']),DEcode_header(msg['From']),tex,tex21,tex22,a

def GetMailNum(a,nm,get):
    global d1,d2,d3,tex
    if a>nm or a<1:
        raise ValueError
    num_mail=bytes(str(a),'utf-8')
    _,data=get.fetch(num_mail,"(BODY.PEEK[])")
    msg=email.message_from_bytes(data[0][1])
    print('Дата',msg['DATE'])
    print('Тема письма:'+DEcode_header(msg['Subject']))
    print('Отправитель:'+DEcode_header(msg['From']))
    print('Вложенные файлы будут записаны в: /home/aleksey')
    msg2=''
    
    for x in msg.walk():        
        if x.get_content_type()=="multipart":
            continue
        elif x.get_content_type()=="text/plain":
            print('Текст вашего собщения:')
            print(x.get_payload(decode = True).decode('utf-8'))
            tex=x.get_payload(decode = True).decode('utf-8')
            for xi in re.findall(r'(https://.{40}).+',tex):
                print(xi)
                if input('перейти по ссылке? (любая кнопка):'):
                    URL_transition(xi)
            print()    
        elif x.get_content_type()=="text/html":
            print()
            N=int(input('html-текст Сколько знаков вывести? : '))
            print()
            print(x.get_payload(decode = True).decode('utf-8')[:N])
            msg2=x.get_payload(decode = True).decode('utf-8')
            print()
            print('Найдены такие ссылки:')
            print()
            for x in re.findall(r'<a.+href="(https://.{40})',msg2):
                print(x)
                if input('перейти по ссылке? (любая кнопка):'):
                    URL_transition(x)
            print()    
            print('Найдены ссылки связанные с изображениями :')
            print()
            for x in re.findall(r'<img.+src="(.{80})',msg2):
                print(x)
                if input('перейти по ссылке? (любая кнопка):'):
                    URL_transition(x)
                print()    
        elif x.get_content_maintype()=="image":
            if x.get_content_maintype() != 'multipart' and x.get('Content-Disposition') is not None:
                open('/home/aleksey' + '/' + DEcode_header(x.get_filename()), 'wb').write(x.get_payload(decode='utf-8'))
        elif x.get_content_maintype() != 'multipart' and x.get('Content-Disposition') is not None:
            open('/home/aleksey' + '/' + DEcode_header(x.get_filename()), 'wb').write(x.get_payload(decode='utf-8'))
            
               
        

def GetMaill(cervice,login):
    if len(cervice)==0 or len(login)==0:
        raise  ValueError
    imap = imaplib.IMAP4_SSL(cervice)
    #imap.login(login, getpass.getpass())
    imap.login(login,'01021979a')
    return imap

def search(get2,get):
    print('У вас {} писем'.format(get2[0].decode('utf-8')))
    nm=int(get2[0].decode('utf-8'))
    text=['Введите номер письма:','Введите дату письма (пример:2018-11-20):',
          'Введите дни(кол) от сегодняшней даты для поиска:',
          'Введите отправителя (лат):','Введите текст:',
          'Сколько последних писем в поиске:','Введите текст:',
          'Поиск по отправителю(4)','Поиск по дням(3)',
          'Поиск по номеру(1)','Поиск по дате(2)',
          'Поиск по фрагменту в письме(5)','Поиск непрочитанных сообщений(6)',
          'Поиск по теме(7)']
    num_def=['GetMailNum(int(b),nm,get)','Search_data(b,get)',
             'Search_timedelta(b,get)','Search_from_subject(b,get,"FROM")',
             'Search_text(b,get)','Search_unseen(b,get)',
             'Search_from_subject(b,get,"Subject")']
    print(text[7:])
    a=int(input())
    if a not in [1,2,3,4,5,6,7]:
        raise  ValueError
    b=input((text[a-1]))
    exec(num_def[a-1])    
    
def menu():
    global get
    while True:
        text='''По умолчанию:
            ukr.net   login:aleksey1652@ukr.net
            Желаете изменить? (д/н):'''
        text2=['Введите имя почты:','Введите логин:']
        
        try:
            a=str(input(text))
            if len(a)==0:
                raise  ValueError
            if a in ['y','д']:
                get=GetMaill('imap.'+input(text2[0]),input(text2[1]))
                _,get2=get.select('INBOX')
                search(get2,get)
            elif a in ['n','н']:    
                get=GetMaill('imap.ukr.net','aleksey1652@ukr.net')
                _,get2=get.select('INBOX')
                search(get2,get)
                #get.logout()
                break
            else:
                raise  ValueError                
                
        except  ValueError:
            print('ошибка')            
            break
   
   
menu()
if subl:
    print(subl)


#def genf():
#    if subl:
#        if subl[0]!='нету':
#            for i in [GetMailNum2(x,get) for x in subl]:
#                yield i
    
    
#hh=genf()    
    
#def rgenf(subl,hh):
#    d=[]
#    if subl:
        
#        if subl[0]!='нету':        
#            for x in hh:
#                d.append(x)
#    return d        
            
#hh1=rgenf(subl,hh)
#print(hh1)
from ma.models import namm,inmaill

def dbfill(hh1):
    htmlt1,htmlt2='',''
    for x in hh1[4]:
        htmlt1=htmlt1+' '+x
    for x in hh1[5]:
        htmlt2=htmlt2+' '+x
    if namm.objects.filter(namail=hh1[2]).count()==0:
        a=namm(namail=hh1[2])
        a.save()
    else:
        a=namm.objects.get(namail=hh1[2])
    a.inmaill_set.create(numail=hh1[6],seen=True,datamail=hh1[0],subj=hh1[1],
                         text=hh1[3],htmlt1=htmlt1,htmlt2=htmlt2)

#dbfill(hh1)

def genf():
    if subl:
        if subl[0]!='нету':
            for i in [GetMailNum2(x,get) for x in subl]:
                  dbfill(i)

genf()                  
    


        
        
        
    
