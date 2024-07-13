from django.shortcuts import redirect, render

from user_management.forms import UserManagmentForm
from .models import UserManagment
# Create your views here.


def home(request):
    return render(request, 'home.html')

def user_create_view(request):
    if request.method == 'POST':
        form = UserManagmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_success_view')
    else:
        form = UserManagmentForm()
    
    for field in form.fields:
        form.fields[field].widget.attrs.update({'class': 'form-control'})
    
    return render(request, 'user_management.html', {'form': form})



def user_success_view(request):
    return render(request, 'user_management_success.html')

def all_user_view(request):
    users = UserManagment.objects.all().order_by('-id')
    return render(request, 'all_users.html', {'users': users})