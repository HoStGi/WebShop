from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


def logoutuser(request):
    logout(request)
    return redirect('home')

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'client/signupuser.html', {'form': form})

def  login_view(request):
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
