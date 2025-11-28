from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from admin_app.models import Profile, Project, Skill,Experience
# Create your views here.
def portfolio_view(request):
    profile = Profile.objects.first()  # or filter by user if needed
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    

    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        
    }
    return render(request, 'portfolio.html', context)

# Default credentials
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            # Store a session variable to mark user as logged in
            request.session["is_admin_logged_in"] = True
            return redirect("admin_page")
        else:
            return render(request, "admin_login.html", {"error": "Invalid username or password!"})
    return render(request, "admin_login.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# from .forms import ContactForm

# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your message has been sent successfully!")
#             return redirect('contact_view')  # redirects to same page or another success page
#     else:
#         form = ContactForm()

#     return render(request, 'portfolio.html', {'form': form})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save directly to DB
        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, "Your message has been sent successfully!")
        return redirect('portfolio_view')

    return render(request, 'portfolio.html')

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from groq import Groq
# import json

# client = Groq(api_key=settings.GROQ_API_KEY)

# @csrf_exempt
# def ai_chat(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         user_message = data.get("message")

#         if not user_message:
#             return JsonResponse({"reply": "Please type something."})

#         try:
#             response = client.chat.completions.create(
#                 model="llama-3.3-70b-versatile",
#                 messages=[
#                     {"role": "system", "content": "You are Mukesh’s portfolio AI assistant. Respond clearly and friendly."},
#                     {"role": "user", "content": user_message}
#                 ]
#             )

#             reply = response.choices[0].message.content   # ✔ FIXED
#             return JsonResponse({"reply": reply})

#         except Exception as e:
#             return JsonResponse({"reply": f"Error: {str(e)}"})

#     return JsonResponse({"reply": "Invalid request"})
