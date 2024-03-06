from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import RegisterForm, LoginForm
from .models import Users

def welcome_site(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())

def register_user(request):
    #pewnie trzeba coś dodać do tego kodu albo podmienić
    #póki co poniższy kod umożliwiwa wyświetlenie formularzy
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #kod który robi coś z wprowadzonymi danymi [backend]
            #jest już kod jakiś napisany, ale trzeba będzie tutaj ogarnąć jeszcze autentyfikację i szyfrowanie hasła
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = Users.objects.create(username=username, password=password, email=email)
            #trzeba bedzie utworzyc te pola w models.py zeby działało (tyle poki co ogarniam xd)
            #bo poki co, po kliknieciu "register" wypierdala błąd, że nie ma tych pól ;pp

            user.save()
    else:
        #kod umozliwiajcy wyswietlenie formularzy
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    #póki co tylko wyswietla formularz
    #trzeba dopisać kod, który obsłuży dane do logowania
    form = LoginForm()
    return render(request, 'login.html', {'form': form})