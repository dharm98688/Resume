from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'Projects.html')


def experience(request):
    exp = [
        {"Company": "Onetechway",
         "Position": "Python Django",
         "yoe": '2018 - 2019'},
        {"Company": "Samgaur Insights",
         "Position": "Project Associate",
         "yoe": '2021 - 2023'},
    ]
    return render(request, 'Experience.html', {"experience": exp})


def certificate(request):
    certi = [
        {'Institution': 'Durga Software Solutions',
         'Course': 'Python'},

        {'Institution': 'Durga Software Solutiions',
         'Course': 'Python FullStack Web Development '},

        {'Institution': 'Aptron Private Solutions.',
         'Course': 'Java'}
    ]
    return render(request, 'Certificates.html', {'certificates': certi})


def contact(request):
    return render(request, 'contact.html')


def resume(request):
    resume_path = 'myapp/DharmRaj.pdf'
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment';
            filename = "DharmRaj.pdf"
            return response
    else:
        return HttpResponse("Resume Not Found")
