from django.shortcuts import render

from main.models import Experience, Education


def show_main(request):
    context = {
        "username": "Rapcuyyy",
        "name": "Rafa Darussalam",
        "npm": "2506538924",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia"
            " | Passionate about Software Engineering, Web Development, and Game Development"
            " | Actively exploring diverse experiences, from teaching assistantships and student organizations to committees and internship opportunities."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rafa Darussalam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Rafa Darussalam",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)