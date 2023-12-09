from django.http import HttpResponse


def index(request):
    data = {
        "name": "고동우",
        "nickname": "ko",
        "age": 24,
    }
    return HttpResponse(data)