from django.http import JsonResponse

def respond_thanks(request):
    return JsonResponse({'message': 'thanks from core 2 of app2'})
