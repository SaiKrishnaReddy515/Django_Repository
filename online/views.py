from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def index(request):
    return render(request,"home.html")

def home(request):
    return render(request,'home.html')

def Login(request):
    return render(request,'Login.html')

def Sign(request):
    return render(request,'SignUp.html')
def end(request):

    return render(request,'Thankyou.html')

def MakeOrder(request):
    return render(request,'home.html')
def Biriyani(request):
    return render(request,'Biriyani.html')
def Meals(request):
    return render(request,'Meals.html')

def FastFoods(request):
    return render(request,'FastFoods.html')

def Tifins(request):
    return render(request,'Tifins.html')

def IceCreams(request):
    return render(request,'Icecreams.html')

def LogOut(request):
    return render(request,'home.html')
def SignUp_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Login.html')

    else:
        form=UserCreationForm()

    return render(request,'SignUp.html',{'form2':form})



def Login_view(request):

    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request,'OrderDetails.html')

    else:
        form=AuthenticationForm()

    return render(request,'Login.html',{'form2':form})

