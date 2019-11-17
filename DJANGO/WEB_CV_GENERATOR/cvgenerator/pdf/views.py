from django.shortcuts import render, redirect
from pdf.models import Profile
from django.http import HttpResponse
from django.template import loader
import io
import pdfkit  # kütüphaneyi dahil etmeyi unutma!


# pip install pdfkit -> pdf yazmamızı kolaylaştıran kütüphane
# https://pypi.org/project/pdfkit/ kütüphane için detaylı kılavuz
# https://wkhtmltopdf.org/  -> incelemekte faydalı olan site (html to pdf)
# indirdiğin MXE versiyonu çıkart ve bin klasörünün yolunu ortam değişkenlerine ekle
def accept(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)
        profile.save()
        return redirect('resume', id=profile.id)  # parametre ile öbür view'a redirect yapıyoruz
    return render(request, 'pdf/accept.html')


def resume(request, id):
    profile = Profile.objects.get(id=id)
    context = {
        'profile': profile
    }
    template = loader.get_template('pdf/resume.html')  # template'i değişkene atadık
    html = template.render(context)  # templateimiz data aldığından içeri data olarak context'i yolladık
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }  # ayarları belirledik.
    pdf = pdfkit.from_string(html, False, options)  # html değişkenini pdf olarak yazacak, ayarları options olacak
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response


def list(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'pdf/list.html', context=context)
