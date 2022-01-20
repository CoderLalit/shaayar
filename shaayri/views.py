from django.shortcuts import render,redirect
from poetrydb.models import Poem
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            poem = Poem.objects.all()
            return render(request, 'Read.html', {'user': user, 'poems':poem})
        
        else:
            messages.error(request, 'Either username or password is incorrect')

    return render(request, 'Home.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def read(request):
    poem = Poem.objects.all()

    if request.method == "POST":
        query = str(request.POST["search_query"])
        
        print('query : ',query)

    return render(request, 'Read.html', {'poems' : poem})

def dashboard(request):
    curr_user = request.user
    user = curr_user.username
    poem = Poem.objects.filter(author=user)

    if request.method == "POST":
        lang = request.POST["poem_lang"]
        author = user
        title = request.POST["poem_title"]
        content = request.POST["poemContent"]

        poem = Poem.objects.create(lang=lang, author=author, title=title, content=content)
        poem.save()

        return redirect("/dashboard")
     
    print('logged in user : ', curr_user.username)
    return render(request, 'dashboard.html', {'user':user, 'poems':poem})


def focus(request, poem_id):
    poem = Poem.objects.get(poemID=poem_id)
    return render(request, 'focus.html', {'poem': poem})

def edit(request, poem_id):
    poem = Poem.objects.get(poemID=poem_id)

    if request.method == "POST":
        try:
            title = str(request.POST["poem_title"])
            content = str(request.POST["poem_content"])

            poem.title = title
            poem.content = content

            poem.save(update_fields=['title', 'content'])
            messages.success(request, 'your poem is successfully updated')
        
        except:
            messages.error(request, 'something went wrong pls try again')

    return render(request, 'edit.html', {'poem': poem})

def delete(request, poem_id):
    poem = Poem.objects.filter(poemID=poem_id)
    poem_obj = Poem.objects.get(poemID=poem_id)

    curr_user = request.user
    user = curr_user.username
    poem_by_author = Poem.objects.filter(author=user)

    try:
        poem.delete()
        msg = 'successfully deleted poem titled : ' + poem_obj.title
        return render(request, 'dashboard.html', {'message':  msg, 'poems': poem_by_author})
    except:
        msg = 'something went wrong. Could not delete : ' + poem_obj.title
        messages.error(request, msg)