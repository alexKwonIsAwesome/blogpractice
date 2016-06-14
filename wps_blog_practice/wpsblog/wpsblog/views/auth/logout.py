from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse

def logout(request):
    auth_logout(request)
    return redirect(reverse("home"))
