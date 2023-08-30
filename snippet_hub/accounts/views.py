from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    # Your logic for fetching user profile info here. 
    # For this example, we're assuming that you have a related Profile model.
    user = request.user
    profile = user.profile  # Replace with how you get your profile information
    context = {
        'user': user,
        'profile': profile
    }
    
    return render(request, 'profile.html', context)
