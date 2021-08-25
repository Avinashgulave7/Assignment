from django.shortcuts import render,redirect
from .models import POST
from .forms import CustomRegistrationForm,PostForm
from django.views import View
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@login_required()
def home(request):
    p=POST.objects.filter(user=request.user)
    return render(request,'app/home.html',{'p':p})

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})

    def post(self,request):
        form=CustomRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Ragistered Succesfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})

@method_decorator(login_required,name='dispatch')

class AddPostView(View):
    def get(self,request):
        form=PostForm()
        return render(request, 'app/addpost.html',{'form':form})

@login_required()
def addpost(request):
    if request.method == 'POST':
        name=request.user
        text=request.POST.get('text')

        a=POST(user=name,text=text)
        messages.success(request, 'Congratulations!! Add Post Succesfully')

        a.save()
        return redirect('/')

def updatepost(request,id):
    p=POST.objects.get(id=id)
    if request.method == 'POST':
        name=request.user
        text=request.POST.get('text')

        p.user=name
        p.text=text

        messages.success(request, 'Congratulations!! update Post Succesfully')

        p.save()
        return redirect('/')

    return render(request, 'app/updatepost.html',{'p':p})


