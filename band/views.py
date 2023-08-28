from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    """
    View function for user login.

    This view handles both GET and POST requests. When a user accesses the login page via GET request,
    it displays the login form. When the user submits the form via POST request, it attempts to authenticate
    the user and log them in if the credentials are valid.

    Parameters:
        - request: The HTTP request object.

    Returns:
        - If the request method is GET, it renders the login form.
        - If the request method is POST and authentication is successful, it redirects to the 'home' page.
        - If the request method is POST and authentication fails, it re-renders the login form with error messages.

    Template:
        - Renders 'band/login.html' template with the login form.
    """
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
    """
    View function for the home page.

    This view is protected by the 'login_required' decorator, ensuring that only authenticated users
    can access it. It renders the 'band/home.html' template, which represents the home page of the website.

    Parameters:
        - request: The HTTP request object.

    Returns:
        - Renders 'band/home.html' template.
    """
    return render(request, 'band/home.html')

def albums(request):
    """
    View function for the albums page.

    Add logic here to fetch and display the album list.

    Parameters:
        - request: The HTTP request object.

    Returns:
        - Renders 'band/albums.html' template.
    """
    # Add logic to fetch and display the album list
    return render(request, 'band/albums.html')

def members(request):
    """
    View function for the members page.

    Add logic here to fetch and display the member list.

    Parameters:
        - request: The HTTP request object.

    Returns:
        - Renders 'band/members.html' template.
    """
    # Add logic to fetch and display the member list
    return render(request, 'band/members.html')
