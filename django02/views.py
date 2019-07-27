from django.shortcuts import render, HttpResponse
from django02 import models


# Create your views here.

def ORMTest(request):
    if request.method == 'GET':
        return render(request, "Orm/index.html")
    name1 = request.POST.get("stu_name")
    age1 = int(request.POST.get("stu_age"))
    print(type(name1), type(age1))
    # 方法一
    student = models.student.objects.create(name=name1, age=age1)
    # 方法二
    #student = models.student(name=name1, age=age1)
    #student.save()
    getstudent = models.student.objects.get(name=name1)
    if (getstudent):

        return HttpResponse("上传的数据保存成功!")
    else:
        return HttpResponse("上传的数据失败!")
