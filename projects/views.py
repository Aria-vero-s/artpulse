from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CollaborativeProject
from .forms import CollaborativeProjectForm


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
        return redirect('user_profile', username=request.user.username)
    
    return render(request, 'create_project.html')

@login_required
def project_detail(request, project_id):
    project = CollaborativeProject.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def interested_toggle(request, project_id):
    project = CollaborativeProject.objects.get(id=project_id)
    user = request.user

    if user in project.interested_users.all():
        project.interested_users.remove(user)
    else:
        project.interested_users.add(user)

    return redirect('user_profile', username=project.user.username)


@login_required
def update_project(request, project_id):
    project = get_object_or_404(CollaborativeProject, id=project_id, user=request.user)

    if request.method == 'POST':
        form = CollaborativeProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = CollaborativeProjectForm(instance=project)

    return render(request, 'update_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(CollaborativeProject, id=project_id, user=request.user)

    if request.method == 'POST':
        project.delete()
        return redirect('user_profile', username=request.user.username)

    return render(request, 'delete_project.html', {'project': project})