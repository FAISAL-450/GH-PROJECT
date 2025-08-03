from django.urls import path
from .views import project_list, project_form, project_delete
urlpatterns = [
    path("", project_list, name="project_list"),  # Display project list with filtering and pagination
    path("form/", project_form, name="project_create"),  # Create a new project
    path("form/<int:id>/", project_form, name="project_edit"),  # Edit an existing project
    path("delete/<int:id>/", project_delete, name="project_delete"),  # Delete a project
]
