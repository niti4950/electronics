from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import Contact_form,LoginForm, RegisterForm
from django.contrib.auth import get_user_model

def home_page(request):
    context = {
        "title":'Home page',
        "content":"this is contact page",
    }
    print(request.session.get('first_name',"unknown"))
    if request.user.is_authenticated():
        context['Premium'] = "YEAHH YOU ARE PREMIUM USER"
    return render(request, 'home_page.html',context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form,

    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            return redirect('/login')
        else:
            print('error')

        context['form'] = LoginForm()
    return render(request, 'auth/login_page.html',context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request, 'auth/register_page.html',context)

def about_page(request):
    context = {
        "title": 'About page',
        "content": "this is contact page",
    }
    return render(request, 'home_page.html',context)

def contact_page(request):
    contact_form = Contact_form(request.POST or None)

    context = {
        "title": 'Contact page',
        "content":"this is contact page",
        "form": contact_form,
        #"brand":'New brand'
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html',context)
