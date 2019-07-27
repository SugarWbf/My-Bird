from django.shortcuts import render,HttpResponse
from django03 import form as forms
# Create your views here.
def useForm(request):
    if request.method == 'POST':
        form = forms.addNum(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            name = form.cleaned_data['name']
            s = a + b
            result = {"s":s,"name":name}
            return render(request,"Form/result.html",{"result":result})
        pass
    else:
        form = forms.addNum()
        return render(request,"Form/index.html",{"form":form})
