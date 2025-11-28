from django.shortcuts import render,redirect, get_object_or_404
from .models import Project,Experience,Skill,Profile,Tool
from .forms import ProjectForm
from django.contrib import messages
from .forms import ExperienceForm



# Create your views here.
def admin_page(request):
    # if not request.session.get('admin_logged_in'):
    #     return redirect('admin_login')

    context = {
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'profiles': Profile.objects.all(),
    }

    return render(request, 'admin_page.html', context)

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'project_list.html', {'projects': projects})

# Add new project
# def project_create(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.save()

#             # Handle Select2 "tag" tools (new ones not yet in DB)
#             tool_names = request.POST.getlist('tools')
#             for name in tool_names:
#                 tool, created = Tool.objects.get_or_create(name=name)
#                 project.tools.add(tool)

#             return redirect('project_list')
#     else:
#         form = ProjectForm()
#     return render(request, 'project_form.html', {'form': form})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            tools = request.POST.getlist('tools[]')  # get list of tools from Select2
            project.tools = ','.join(tools)  # save as comma-separated
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form, 'tools_list': []})

# Edit existing project
# def project_update(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES, instance=project)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.save()

#             # Clear old tools, add updated ones
#             project.tools_used.clear()
#             tool_names = request.POST.getlist('tools_used')
#             for name in tool_names:
#                 tool, created = Tool.objects.get_or_create(name=name)
#                 project.tools.add(tool)

#             return redirect('project_list')
#     else:
#         form = ProjectForm(instance=project)
#     return render(request, 'project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            tools = request.POST.getlist('tools[]')
            project.tools = ','.join(tools)
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
        tools_list = project.get_tools_list()  # prefill tools
    return render(request, 'project_form.html', {'form': form, 'tools_list': tools_list})

# Delete project
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'project': project})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Skill
from .forms import SkillForm

# List all skills
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skill_list.html', {'skills': skills})

# Add a new skill
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'skill_form.html', {'form': form})

# Edit a skill
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'skill_form.html', {'form': form})

# Delete a skill
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'skill_delete.html', {'skill': skill})

from .models import Profile
from .forms import ProfileForm

# List all profiles
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

# Add new profile
def profile_create(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('profile_list')
    return render(request, 'profile_form.html', {'form': form})

# Edit profile
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_list')
    return render(request, 'profile_form.html', {'form': form})

# Delete profile
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'profile_delete.html', {'profile': profile})

def experience_list(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'experience_list.html', {'experiences': experiences})

# Add new experience
def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience added successfully!')
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'add_experience.html', {'form': form})

# Edit existing experience
def edit_experience(request, exp_id):  # must match URL parameter name
    exp = get_object_or_404(Experience, id=exp_id)
    
    if request.method == "POST":
        form = ExperienceForm(request.POST, request.FILES, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=exp)
    
    return render(request, 'edit_experience.html', {'form': form, 'exp': exp})

# Delete experience
def delete_experience(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    exp.delete()
    messages.success(request, 'Experience deleted successfully!')
    return redirect('experience_list')

def admin_logout(request):
    # Clear session
    request.session.flush()
    return redirect("portfolio_view")

from user_app.models import Contact
def contact_list_view(request):
    contacts = Contact.objects.all().order_by('-created_at')  # newest first
    return render(request, 'contact_list.html', {'contacts': contacts})