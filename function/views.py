
from django.shortcuts import render
from datetime import datetime

from function.models import formsubmit,userjourneydata,comments


# def getphoto(file):
#     binarydata = file.read()
#     return binarydata

def firstpage (request):
    return render(request, "homepage.html")
def secondpage (request):
    if request.method== "POST":
        image = request.FILES.get('photo')
        desc = request.POST.get('Description')
        locate = request.POST.get('lo_cation')
        name = request.POST.get('journey_name')
        form = formsubmit(photo =image, description = desc, location =locate,journeyname=name,date=datetime.today())
        form.save()
    return render(request, "addlog.html")
def thirdpage (request):
    if "cmtsub" in request.POST:
        cmt = request.POST.get('comment')
        id = request.POST.get('secret2')
        form = comments(key = id,comments=cmt)
        form.save()
        data = userjourneydata.objects.filter(key = id).values('name','journeyname','personimage','key').distinct()
        data1 = userjourneydata.objects.filter(key = id).values('placelocation','photo','date','description','keyid','key')
        data2 = comments.objects.filter(key=id)
        return render(request,"profiles.html",{"prof" : data,'profuniq':data1,'cmt':data2})

    elif "profsub" in request.POST:
        key = request.POST.get('profsub')
        id = request.POST.get('secret')
        data = userjourneydata.objects.filter(keyid = key,key=id).values('name','journeyname','personimage','journeylocation','placelocation','photo','date','description','key')
        return render(request,"gallery.html",{'prof': data})
        
    elif "btnsub" in request.POST:
        key = request.POST.get('btnsub')
        data = userjourneydata.objects.filter(key = key).values('name','journeyname','personimage','key').distinct()
        data1 = userjourneydata.objects.filter(key = key).values('placelocation','photo','date','description','keyid','key')
        data2 = comments.objects.filter(key=key)
        return render(request,"profiles.html",{"prof" : data,'profuniq':data1,'cmt':data2})

    elif  request.method == "POST":
            profile = request.POST.get('search')
            data = userjourneydata.objects.filter(name = profile).values('name','journeyname','personimage','journeylocation','key').distinct()
            data1 = userjourneydata.objects.filter(name = profile).count()
            if not data.exists():
                data = userjourneydata.objects.filter(journeylocation = profile).values('name','journeyname','personimage','journeylocation','key').distinct()
                data1 = userjourneydata.objects.filter(journeylocation = profile).count()
            # stu = {"profiles": data}
            # data2 = {"data1" : data1}
            return render(request, "search.html",{"profiles": data,"data1" : data1})
    
    else:
        return render(request,"search1.html")

def fourthpage(request):
    form = formsubmit.objects.values('location','photo','date','description','journeyname')
    return render(request,"userprofile.html",{'profuniq':form})
