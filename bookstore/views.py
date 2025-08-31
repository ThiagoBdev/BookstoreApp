from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
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


def hello_world(request):
    return HttpResponse("Hello, World!")

