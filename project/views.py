from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

# List view – Display, filter, and paginate projects
def project_list(request):
    query = request.GET.get("q", "")  # Defaults to empty if no query string
    projects = Project.objects.all().order_by("id")  # Changed from "-id" to "id"
    if query:
        projects = projects.filter(name_of_project__icontains=query)

    paginator = Paginator(projects, 10)
    page_number = request.GET.get("page")
    try:
        projects_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        projects_page = paginator.get_page(1)

    return render(request, "project/project_list.html", {
        "projects": projects_page,
        "query": query
    })

# Create & Update view – Handle data entry form
def project_form(request, id=None):
    project = get_object_or_404(Project, id=id) if id else None

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project saved successfully.")
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)

    return render(request, "project/project_form.html", {"form": form})

# Delete view – Remove project entry
def project_delete(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    messages.warning(request, f"Project '{project.name_of_project}' deleted.")
    return redirect("project_list")

