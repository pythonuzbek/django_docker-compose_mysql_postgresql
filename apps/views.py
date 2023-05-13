from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.models import User

from django.http import JsonResponse
# from httpx_client import get_data
@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        data = request.POST.get('my_data')
        User.objects.create(data['name'],
                            password=data['password'])
        User.save()



# def my_view(request):
#
#     return JsonResponse({'message': f'Received data: {data}'})