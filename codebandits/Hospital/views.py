from django.shortcuts import render
from .models import State,City,Hospital
# Create your views here.
def Home(request):
    if(request.method=='POST'):
        citylist=list(City.objects.all())
        hospitallist=list(Hospital.objects.all())
        hosp=[]
        for c in hospitallist:
            n=c.City.Name
            print(n)
            if request.POST.get("city")==n:
                hosp.append(c)
        return render(request,'index.html',{'hl':hosp,'cl':citylist})
    else:       
        hospitallist=list(Hospital.objects.all())
        citylist=list(City.objects.all())
        return render(request,'index.html',{'hl':hospitallist,'cl':citylist})