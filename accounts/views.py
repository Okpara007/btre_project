from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts

# Create your views here.
def register(request):
    if request.method == 'POST':
        # get form values(into variables)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # form validation
        # check if passwords match 
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else: # check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already exists')
                    return redirect('register')
                else:
                    # register user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # if you want the user to login imediately after registration 
                    # auth.login(request, user) 
                    # messages.success(request, 'You are now logged in') 
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You have successfully registered')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
         # Login User logic goes here
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: # means user is found
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id) # to get contacts or inquiries of a certain user(logged in user) which can be gotten by using request.user

    context = {
        'contacts': user_contacts
    }
    return render (request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       messages.success(request, 'You are now logged out')
       return redirect('index') # redirect has to be imported
