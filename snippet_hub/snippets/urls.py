from django.urls import path
from . import views

app_name = 'snippets'

urlpatterns = [
    path('', views.home, name='home'),  # Landing page or login page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('new_snippet/', views.new_snippet, name='new_snippet'),  # Create a new code snippet
    path('view_snippets/', views.view_snippets, name='view_snippets'),  # View all code snippets
    path('view_snippets/<int:snippet_id>/', views.view_snippet, name='view_snippet'),  # View a single code snippet
    path('edit_snippet/<int:snippet_id>/', views.edit_snippet, name='edit_snippet'),  # Edit a single code snippet
    path('delete_snippet/<int:snippet_id>/', views.delete_snippet, name='delete_snippet'),  # Delete a single code snippet
    path('copy_snippet/<int:snippet_id>/', views.copy_snippet, name='copy_snippet'),
    path('user/<str:username>/', views.view_user_profile, name='view_user_profile'),
    path('increment_copy_count/<int:snippet_id>/', views.increment_copy_count, name='increment_copy_count'),
]

print(urlpatterns)