from django.shortcuts import render
from .models import Hizmetler,FAQ,Kazanimlar
# Create your views here.


def hakkimizda(request):
    context = {
    }
    return render(request, "hakkimizda.html", context)



def hizmetlerimiz(request):
    pagetitle = "Hizmetlerimiz"
    hizmetler = Hizmetler.objects.all().order_by('id')
    faq = FAQ.objects.all()

   
    context = {
        'pagetitle':pagetitle,
        'hizmetler':hizmetler,
        'faq':faq,
    }
    return render(request, "hizmetlerimiz.html", context)



def kazanimlarimiz(request):
   
    pagetitle = "Kazanımlar"
    kazanimlar = Kazanimlar.objects.all().order_by('id')
    faq = FAQ.objects.all()
    context = {
        'pagetitle':pagetitle,
        'kazanimlar':kazanimlar,
        'faq':faq,
    }
    return render(request, "kazanimlarimiz.html", context)
