# from django.shortcuts import render, HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .forms import ImageForm
from .models import Image
# Create your views here.

def index(request):
    return render(request, 'index.html')

# def xray(request):
#     return render(request, 'xray.html')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'xray.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
        img=Image.objects.all()
    return render(request,"xray.html",{"img":img,"form":form})

def register(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        role = request.POST.get('role')        
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(full_name = full_name,username=username,email=email,password=password,role=role)
                user.save()
                messages.info(request,'User created')
                if User.objects.filter(role='doctor'):
                    return redirect('doctorLogin')
                elif User.objects.filter(role='patient'):
                    return redirect('patientLogin')
        else:
            messages.info(request,'Password incorrect')
    else:
        return render(request,'register.html')

def patientLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
       
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            In=True
            auth.login(request,user)
            return redirect('/',{'user':user})
        else:
            messages.info('Invalid Credentials')
            return redirect('patientLogin')
    else:
        return render(request,'patientLogin.html')
    
def doctorLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
       
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            In=True
            auth.login(request,user)
            return redirect('/',{'user':user})
        else:
            messages.info('Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    In=False
    auth.logout(request)
    return redirect('/')

def xray(request):
    return render(request, 'xray.html')
 
