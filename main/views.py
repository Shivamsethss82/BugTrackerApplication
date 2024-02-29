from django.shortcuts import render
from django.http import HttpResponse
from .models import Myform
from django.contrib import messages

# Create your views here.

def home(request):
    thanks = False
    if request.method == "POST":
        bug_title = request.POST.get('bug-title','')
        issue_description = request.POST.get('issue-description','')
        os = request.POST.get('os','')
        browser = request.POST.get('browser','')
        assigned_to = request.POST.get('assign','')
        priority = request.POST.get('priority','')
        status = request.POST.get('status','')
        screenshot = request.FILES.get('screenshot', None)
        print(bug_title, issue_description, os, browser, assigned_to, priority, status)
        contact = Myform(
            bug_title=bug_title,
            issue_description=issue_description,
            os=os,
            browser=browser,
            assigned_to=assigned_to,
            priority=priority,
            screenshot=screenshot,
            status=status
        )
        contact.save()
        messages.success(request, 'Bug report submitted successfully!')
        thanks = True
    return render(request, 'home.html', {'thanks': thanks})