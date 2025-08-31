from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git

@csrf_exempt
def update(request):
    if request.method == "POST":
        print("Webhook received!")
        print(request.body.decode())  # Para ver o JSON cru
        return HttpResponse("Webhook received!")
    return HttpResponse("Only POST allowed", status=405)


def hello_world(request):
    return HttpResponse("Hello, World!")

