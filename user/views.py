from django.shortcuts import render
from .forms import createUser, UpdateUser
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = createUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your account has been successfully created')
            return redirect('users:login')
    else:
        form = createUser()
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        user_update_form = UpdateUser(request.POST, instance = request.user )
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request,'your account has been updated successfully')
            return redirect('users:profile')
    else:
        user_update_form = UpdateUser(instance = request.user )
        context = {
            'update_form':user_update_form
        }
        return render(request,'profile.html',context)

    
