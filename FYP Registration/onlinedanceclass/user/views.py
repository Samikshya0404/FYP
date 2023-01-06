from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import JsonResponse
from .models import Styles
from .serializers import StylesSerializer

def home(request):
    return render(request, 'user/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

def style_list(request):
    styles = Styles.objects.all()
    serializer = StylesSerializer(styles, many=True)
    return JsonResponse(serializer.data, safe=False)


