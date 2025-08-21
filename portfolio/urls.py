from django.urls import path
from . import views
from django.conf.urls.static  import static
from django.conf import settings
urlpatterns =  [
   path('', views.home ,name="home"),
   path('sendmail/',views.sendmail,name='sendmail'),  
   path('success/',views.success,name='success'),    

     

]
