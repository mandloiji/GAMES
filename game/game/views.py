from django.shortcuts import render
from technology.models import Tech,NewModel
from .forms import Tech_Form
def home(request):
    return render(request,'index.html')

def about(request):
    a=Tech.objects.get(id=1)
    return render(request,'about.html',{'d':a})

def contact(request):
    if request.method== 'post':
       r=NewModel(request.post)
       if r.is_valid():
        n=r.cleaned_data['name']
        e=r.cleaned_data['email']
        p=r.cleaned_data['phone']
        d=r.cleaned_data['Device']
        t=NewModel(name=n,email=e,phone=p,Device=d)
        t.save()
        r=NewModel()
    else:

        
        t=Tech_Form()
    data=NewModel.objects.all()
    return render(request,'contact.html',{'c':t,'data':data})

def product(request):
    s=Tech.objects.get(id=2)
    return render(request,'product.html',{'r':s})

def best(request):
    s='lorem mnfsduhyf8uhsdkjryhjbgyhujhgtyujhyujkhdsifewhfiuew jhyruhuhuweyrhjkbn bhhyuihyu htyub uyubjhyr8ubhjgyghbuyuhu'
    return render(request,'best.html',{'str':s})

def remot(request):
    
    return render(request,'remot.html')

def video(request):
   
    
    return render(request,'video.html')