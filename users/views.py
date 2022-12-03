from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms import SignupForm


def signup(request):
    """
    Used for user registration
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})
