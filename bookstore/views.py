from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
    import json
    from django.http import JsonResponse

    if request.method == "POST":
        event = request.headers.get("X-GitHub-Event")
        if event == "ping":
            return JsonResponse({"msg": "pong"})
        # Atualização real do repo
        repo = git.Repo('/home/ThiagoBdev/BookstoreApp')
        origin = repo.remotes.origin
        origin.pull()
        return JsonResponse({"msg": "Updated code on PythonAnywhere"})
    return HttpResponse("Only POST allowed", status=405)