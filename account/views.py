from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = str(request.POST['pass1'])
        pass2 = str(request.POST['pass2'])
 
        user = auth.authenticate(username=username)

        if user is not None:
            print('username already taken')
            messages.error(request, 'username already taken')
        
        elif pass2 != pass1:
            print('password did not match.')
            messages.error(request, 'password did not match.')

        else:
            first_name = name.split(' ')[0]
            last_name = name.split(' ')[1]
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=pass1)
            user.save()
            
            return render(request, 'Home.html')
            messages.success(request, 'User Successfully Created')


    return render(request, 'signup.html')