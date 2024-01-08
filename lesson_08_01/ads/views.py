from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Ad

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('index.html')
    context = {"ads": Ad.objects.all(), "test_var": "TEST"}
    return HttpResponse(template.render(context, request))


    # result = "Объявления:\n\n"
    # for ad in Ad.objects.all():
    #     result += str(ad.name) + ' ' + str(ad.content) + ' ' + str(ad.price) + '\n'
    # return HttpResponse(result, content_type="text/plain; charset=utf-8")
