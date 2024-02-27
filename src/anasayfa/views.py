from django.shortcuts import render

# Create your views here.
from kurumsal.models import FAQ
from portfolio.models import PortfolioModel,Projelerimiz
from  haber.models import BlogModel
def anasayfa(request):

    portfolioobjs  = PortfolioModel.objects.order_by('-id')
    blog  = BlogModel.objects.all()
    projeler = Projelerimiz.objects.all().order_by('-id')[:4]
    faq = FAQ.objects.all()
    context = {
        'portfolioobjs':portfolioobjs,
        'blog':blog,
        'projeler':projeler,
        'faq':faq,
    }
    return render(request, "index.html", context)

