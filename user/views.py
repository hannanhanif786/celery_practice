from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# from celerypractice.celery import hello_world
from user.tasks import sub_numbers, sum_numbers

@require_http_methods(["GET"])
def home(request):
    sub_numbers.delay(7, 1)
    sub_numbers.delay(9, 1)
    sum_numbers.delay(5, 5)
    sum_numbers.delay(10, 5)
    return HttpResponse("Any kind of HTML Here")
