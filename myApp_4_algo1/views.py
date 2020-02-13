from django.shortcuts import render
import os
# Create your views here.
def algo1(request):
    #return HttpResponse("myapp2")

    category="cat"

    return render(request, "algo1.html",{"data":category})

def algo1_upload(request):

    File = request.FILES.get("myfile", None)
    image_path = "./myApp_4_algo1/images/"+"%s"%File.name #+ "%s" % File.name

    # 打开特定的文件进行二进制的写操作;
    with open(image_path, 'wb+') as f:
        # 分块写入文件;
        for chunk in File.chunks():
            f.write(chunk)
    category="dog"
    return render(request, "algo1.html",{"data":category},locals())
