from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import Resumeform
from . models import Resume
from django.views import View


def success(request):
    fr = Resumeform()
    candidate = Resume.objects.all()
    return render(request,'core/home.html',{'candid':candidate,'form':fr})


class Homeview(View):
    def get(self,request):
        fr = Resumeform()
        candidate = Resume.objects.all()
        return render(request,'core/home.html',{'candid':candidate,'form':fr})

    def post(self,request):
        form = Resumeform(request.POST,request.FILES)  
        if form.is_valid():
            form.save()     
        #return render(request,'core/home.html',{'form':form})
        return HttpResponseRedirect('/success')

class Candidate(View):
    def get(self,request,pk):
        print(pk)
        candidates= Resume.objects.get(pk=pk)
        return render(request,'core/review.html',{'cand':candidates})

# Create your views here.
