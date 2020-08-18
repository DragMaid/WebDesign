from django.shortcuts import render

# Create your views here.
def show_menu(request):
    return render(request, 'home.html', {})

def new_page(request):
    return render(request, 'new.html', {})

