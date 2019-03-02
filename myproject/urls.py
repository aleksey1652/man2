from django.urls import include,path
from django.contrib import admin

urlpatterns = [
#    path('polls/', include('polls.urls')),
#    path('ma/', include('ma.urls')),
    path('man/', include('man.urls')),
    path('admin/', admin.site.urls),
    
]
