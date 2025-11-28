from django import forms
from .models import Project,Experience,Tool


# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['title','tools', 'description', 'image', 'link']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#             'link': forms.URLInput(attrs={'class': 'form-control'}),
#             'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#         }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tools', 'link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tools': forms.TextInput(attrs={'class': 'form-control', 'id': 'tools-input'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    class Meta:
        model = Project
        fields = ['title', 'description', 'tools', 'image', 'link']

from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
            'proficiency': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Proficiency %', 'min':0, 'max':100}),
        }

from .models import Profile        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'social_link': forms.URLInput(attrs={'class': 'form-control'}),
        }   
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            'company_name',
            'role',
            'duration',
            'description',
            'start_date',
            'end_date',
            'location',
            'image'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
