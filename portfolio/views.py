from django.shortcuts import render , redirect
from django.conf import settings
##from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import FileResponse, Http404
from pathlib import Path
from . models import MainImg, SkillCategory, SkillModel, ProjectModel##,HeaderImg
from . forms import ContactForm

def home(request):
    image = MainImg.objects.all()
    ##headimg = HeaderImg.objects.all()
    projects = ProjectModel.objects.order_by('-id')[:4]
    categories = SkillCategory.objects.prefetch_related("skills").all()
    return render(request, 'portfolio/index.html',{"categories":categories,"projects":projects,"image":image})##"headimg":headimg,

def sendmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form=ContactForm()
    return render(request, 'home.html',{'form':form})
   
def success(request):
    return HttpResponse('Message sent successfully !!!')    
# Create your views here.
