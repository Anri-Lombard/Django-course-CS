from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request):
    # keep data submitted by form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    # recreate empty form
    else:
        form = UserRegistrationForm()
    # direct to this path
    return render(request, 'users/register.html', {'form': form})

# MESSAGES:
#     messages.debug
#     messages.info
#     messages.success
#     messages.warning
#     messages.error


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
