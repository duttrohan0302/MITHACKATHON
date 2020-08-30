from django.shortcuts import render
from .models import State,City,Hospital
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib,base64
# Create your views here.
def Home(request):
    if(request.method=='POST'):
        citylist=list(City.objects.all())
        hospitallist=list(Hospital.objects.all())
        beds=[0,0,0]
        bedsl=['l1beds','l2beds','l3beds']
        hosp=[]
        for c in hospitallist:
            n=c.City.Name
            if request.POST.get("city")==n:
                hosp.append(c)
                beds[0]=beds[0]+c.l1beds
                beds[1]=beds[1]+c.l2beds
                beds[2]=beds[2]+c.l3beds
        plt.pie(beds, labels =bedsl)
        fig=plt.gcf()
        fig.savefig('Hospital/static/Hospital/a.png')
        return render(request,'index.html',{'hl':hosp,'cl':citylist})
    else:
        hospitallist=list(Hospital.objects.all())
        citylist=list(City.objects.all())
        beds=[0,0,0]
        bedsl=['l1beds','l2beds','l3beds']
        for c in hospitallist:
            beds[0]=beds[0]+c.l1beds
            beds[1]=beds[1]+c.l2beds
            beds[2]=beds[2]+c.l3beds

        plt.pie(beds, labels =bedsl)
        fig=plt.gcf()
        fig.savefig('Hospital/static/Hospital/a.png')
        return render(request,'index.html',{'hl':hospitallist,'cl':citylist})

def Index(request):
    if(request.method=='POST'):
        user=request.user
        citylist=list(City.objects.all())
        hospitallist=list(Hospital.objects.all())
        hosp=[]
        for c in hospitallist:
            n=c.City.Name
            if request.POST.get("city")==n:
                hosp.append(c)
        return render(request,'hospital.html',{'hl':hospitallist,'b':user,'cl':citylist})
    else:
        user=request.user
        hospitallist=list(Hospital.objects.all())
        citylist=list(City.objects.all())
        return render(request,'hospital.html',{'hl':hospitallist,'b':user,'cl':citylist})
