from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    # keep data submitted by form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
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
