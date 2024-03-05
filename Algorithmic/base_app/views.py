from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import MyForm
from .models import Users

def welcome_site(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            user = Users.objects.create(name=user_name)
            user.save()
            return HttpResponse('User was created with name ' + user_name)
    else:
        form = MyForm()
    return render(request, 'register.html', {'form': form})