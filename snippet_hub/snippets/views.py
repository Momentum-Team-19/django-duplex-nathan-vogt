from django.shortcuts import render, redirect
from .models import Snippet, Tag
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Import the Q object
from django.contrib.auth.models import User # Import the User model
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'snippets/home.html', {})

def profile(request):
    snippets = Snippet.objects.filter(creator=request.user)  # only fetch snippets created by the current user
    return render(request, 'snippets/profile.html', {'snippets': snippets})

@login_required  # makes sure the user is logged in before they can create a new snippet
def new_snippet(request):
    all_tags = Tag.objects.all()
    if request.method == 'POST':
        snippet_name = request.POST.get('snippet_name')
        snippet_language = request.POST.get('snippet_language')
        snippet_code = request.POST.get('snippet_code')
        snippet_description = request.POST.get('snippet_description')
        is_public = request.POST.get('is_public') == 'on'  # Checkbox returns 'on' if checked
        
        

        new_snippet = Snippet(
            title=snippet_name, 
            language=snippet_language, 
            code=snippet_code, 
            description=snippet_description,
            creator=request.user,  # set the creator to the currently logged-in user
            is_public=is_public,
        )
        new_snippet.save()

        selected_tags = request.POST.getlist('tags')
        new_snippet.tags.set(selected_tags)

    return render(request, 'snippets/new_snippet.html', {'all_tags': all_tags})

def view_snippets(request):
    query = request.GET.get("search", "")  # Get the search query
    if query:
        snippets = Snippet.objects.filter(
            Q(title__icontains=query) |
            Q(language__icontains=query) |
            Q(description__icontains=query) &
            Q(is_public=True)
        )
        # if advanced search
            # add in parameters
            # if each parameter is checked ...
        # search with 1 word if multiple given

    else:
        snippets = Snippet.objects.filter(is_public=True)
    
    return render(request, 'snippets/view_snippets.html', {'snippets': snippets})

def view_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    
    return render(request, 'snippets/view_snippet.html', {'snippet': snippet})

@login_required  # makes sure the user is logged in before they can edit a snippet
def edit_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    all_tags = Tag.objects.all()
    selected_tags = snippet.tags.all() # Get all the tags that are currently selected for this snippet
    
    if request.method == 'POST':
        snippet.title = request.POST.get('snippet_name')
        snippet.language = request.POST.get('snippet_language')
        snippet.code = request.POST.get('snippet_code')
        snippet.description = request.POST.get('snippet_description')
        is_public = request.POST.get('is_public') == 'on'  # Checkbox returns 'on' if checked
        snippet.is_public = is_public

        selected_tags = request.POST.getlist('tags')  # Get the list of tags that were selected in the form
        snippet.save()
        snippet.tags.set(selected_tags)  # update tags for this snippet

        return redirect('snippets:view_snippet', snippet_id=snippet.id) # Redirect to the view page of the updated snippet
    
    return render(request, 'snippets/edit_snippet.html', {'snippet': snippet, 'all_tags': all_tags, 'selected_tags': selected_tags})

@login_required  # makes sure the user is logged in before they can delete a snippet
def delete_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    # Check if the snippet belongs to the current user
    if snippet.creator == request.user:
        snippet.delete()
    return render(request, 'snippets/profile.html', {'snippet': snippet})

@login_required # makes sure the user is logged in before they can copy a snippet
def copy_snippet(request, snippet_id):
    original_snippet = Snippet.objects.get(id=snippet_id)
    original_snippet.copy_count += 1 # Increment the copy count
    original_snippet.save() # Save the updated copy count

    new_snippet = Snippet(
        title=original_snippet.title,
        language=original_snippet.language,
        code=original_snippet.code,
        description=original_snippet.description,
        creator=request.user,
    )

    new_snippet.save()

    # print(f"Copied snippet with ID: {original_snippet.id}")
    # print(f"New snippet created with ID: {new_snippet.id}")
    # print(f"New snippet belongs to: {new_snippet.creator}")

    return redirect('snippets:view_snippets')


def view_user_profile(request, username):
    user = User.objects.get(username=username)
    snippets = Snippet.objects.filter(creator=user)
    return render(request, 'snippets/view_user_profile.html', {'user': user, 'snippets': snippets})


@login_required
def increment_copy_count(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        snippet.copy_count += 1
        snippet.save()
        return JsonResponse({'status': 'success', 'message': 'Copy count incremented'})
    except Snippet.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Snippet does not exist'})

