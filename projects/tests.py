from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CollaborativeProject

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        project = CollaborativeProject.objects.create(
            user=request.user,
            title=title,
            description=description
        )
        return redirect('project_detail', project_id=project.id)
    
    return render(request, 'projects/create_project.html')

@login_required
def project_detail(request, project_id):
    project = CollaborativeProject.objects.get(id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def interested_toggle(request, project_id):
    project = CollaborativeProject.objects.get(id=project_id)
    user = request.user

    if user in project.interested_users.all():
        project.interested_users.remove(user)
    else:
        project.interested_users.add(user)

    return redirect('project_detail', project_id=project_id)
