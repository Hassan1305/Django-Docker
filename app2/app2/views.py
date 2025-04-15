from django.http import JsonResponse

def thanks(request):
    return JsonResponse({'message': 'Thanks from App2!'})
