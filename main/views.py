from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education
from main.forms import ExperienceForm, EducationForm


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

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST":
        input_secret = request.POST.get("secret_code")
        header_secret = request.headers.get("X-Secret-Code")

        if settings.PORTFOLIO_SECRET not in [input_secret, header_secret]:
            messages.error(request, "Akses ditolak: Kode rahasia salah!")
            return redirect("main:show_experience")

        if form.is_valid():
            form.save()
            messages.success(request, "New experience has been added!")
            return redirect("main:show_experience")

    context = {
        "name": "Rafa Darussalam",
        "form": form,
    }
    return render(request, "experiences_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rafa Darussalam",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        input_secret = request.POST.get("secret_code")
        header_secret = request.headers.get("X-Secret-Code")

        if settings.PORTFOLIO_SECRET in [input_secret, header_secret]:
            experience.delete()
            messages.success(request, "Experience berhasil dihapus!")
        else:
            messages.error(request, "Akses ditolak: Kode rahasia salah!")

    return redirect("main:show_experience")

def create_education(request):
    form = EducationForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        input_secret = request.POST.get("secret_code")
        header_secret = request.headers.get("X-Secret-Code")

        if settings.PORTFOLIO_SECRET not in [input_secret, header_secret]:
            messages.error(request, "Akses ditolak: Kode rahasia salah!")
            return redirect("main:show_education")

        if form.is_valid():
            form.save()
            messages.success(request, "New education has been added!")
            return redirect("main:show_education")

    context = {
        "name": "Rafa Darussalam",
        "form": form,
    }

    return render(request, "education_form.html", context)

def edit_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, request.FILES or None, instance=education)

    if request.method == "POST":
        input_secret = request.POST.get("secret_code")
        header_secret = request.headers.get("X-Secret-Code")

        if settings.PORTFOLIO_SECRET not in [input_secret, header_secret]:
            messages.error(request, "Akses ditolak: Kode rahasia salah!")
            return redirect("main:show_education")

        if form.is_valid():
            form.save()
            messages.success(request, "Education data has been updated!")
            return redirect("main:show_education")

    context = {
        "name": "Rafa Darussalam",
        "form": form,
        "education": education,
    }

    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        input_secret = request.POST.get("secret_code")
        header_secret = request.headers.get("X-Secret-Code")

        if settings.PORTFOLIO_SECRET in [input_secret, header_secret]:
            education.delete()
            messages.success(request, "Education berhasil dihapus!")
        else:
            messages.error(request, "Akses ditolak: Kode rahasia salah!")

    return redirect("main:show_education")

def get_education_json(request):
    place_query = request.GET.get("place", "").strip()
    educations = Education.objects.all()

    if place_query:
        educations = educations.filter(place__icontains=place_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    educations = [education.object for education in educations]
    
    place_query = request.GET.get("place", "").strip()

    context = {
        "name": "Rafa Darussalam",
        "education_list": educations,
        "place_query": place_query,
    }

    return render(request, "education.html", context)