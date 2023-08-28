from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'band/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'band/home.html')

def home(request):
    return render(request, 'band/home.html')
  
def albums(request):
    # Add logic to fetch and display the album list
    return render(request, 'band/albums.html')

def members(request):
    # Add logic to fetch and display the member list
    return render(request, 'band/members.html')
