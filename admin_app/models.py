from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tools = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    def get_tools_list(self):
        """Return tools as list for displaying as tags."""
        if self.tools:
            return [t.strip() for t in self.tools.split(',') if t.strip()]
        return []
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.PositiveIntegerField(default=0, help_text="Enter value between 0 and 100")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"        
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    social_link = models.URLField(blank=True, null=True)  # Optional: LinkedIn/Github

    def __str__(self):
        return self.name    
    
# class Service(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
    
#     def __str__(self):
#         return self.title


# class Testimonial(models.Model):
#     name = models.CharField(max_length=100)
#     feedback = models.TextField()
#     rating = models.IntegerField(default=5)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name    

class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='experience_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company_name}"
    
class Tool(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name    