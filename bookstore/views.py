from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
<<<<<<< HEAD
    import git
    from django.http import JsonResponse

    if request.method == "POST":
        repo = git.Repo('/home/ThiagoBdev/BookstoreApp')  
        origin = repo.remotes.origin
        try:
            origin.fetch()
            repo.git.reset('--hard', 'origin/main')  
            return JsonResponse({"msg": "Updated code on PythonAnywhere"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST allowed"}, status=405)
=======
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
>>>>>>> 49dd3138a5e2174c82305c27219a2827b82b7525
