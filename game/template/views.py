from django.shortcuts import render
from technology.models import Techmodel

def home(request):
    s=Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis asperiores necessitatibus laudantium aliquam praesentium! Sapiente corrupti earum modi ab aspernatur aperiam ut laudantium similique! Rem id voluptate dolorum cupiditate nemo.lorem
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis libero dolor magnam doloribus enim maxime cum, cupiditate aliquid, molestias modi reprehenderit neque architecto perferendis illum laborum praesentium, ipsam amet eos.
    
return render(request,'index.html',{'str':s})

def about(request):
    a=Tech.objects.get(id=1)
    return render(request,'about.html',{'d':a})

def contact(request):
    return render(request,'contact.html')

def product(request):
    s=Tech.objects.get(id=2)
    return render(request,'product.html',{'r':s})

def remot(request):
    return render(request,'remot.html')

def video(request):
    return render(request,'video.html')