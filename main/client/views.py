from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserLogin, CustomUserAuthenticationForm

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'client/loginuser.html', {'form':CustomUserAuthenticationForm()})
    else:
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'client/loginuser.html', {'form':CustomUserAuthenticationForm(), 'error':'User didnt match'})
        else:
            login(request, user)
            return redirect('home')

            
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'client/signupuser.html', {'form':CustomUserCreationForm()})
    else:
        print('else прйден')
        if request.POST['password1'] == request.POST['password2']:
            print('if стоим')
            try:
                print('Try пройден')
                user = CustomUser.objects.create_user(request.POST['email'], password=request.POST['password1'])
                print('User пройден')
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'client/signupuser.html', {'form':CustomUserCreationForm(), 'error': 'That username har alredy'})
        else:
            return render(request, 'client/signupuser.html', {'form':CustomUserCreationForm(), 'error': 'Passwrod did not match'})

# Work
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# Work
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'client/signupuser.html'


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'client/signupuser.html', {'form': form})


def  login_view(request):
    """
      Renders Login Form
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form    = CustomUserAuthenticationForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            # messages.success(request, "Logged In")
            return redirect("home")
        else:
            # messages.error("please Correct Below Errors")
            pass
    else:
        form = CustomUserAuthenticationForm()
    context['login_form'] = form
    return render(request, "client/loginuser.html", context)
