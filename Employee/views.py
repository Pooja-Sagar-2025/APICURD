from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def EmployeeDetail(request, id):
    employee = Employee.objects.get(pk = id)
    serializer = EmployeeSerializer(employee)
    return JsonResponse(serializer.data, safe=True)

def EmployeeList(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee)
    return JsonResponse(serializer.data, safe=True)

@csrf_exempt
def EmployeeCreate(request):
    if request.method=="POST":
        json_data = request.body # in request.body is the json data
        stream = io.BytesIO(json_data) # that json data convert to stream
        pythondata = JSONParser().parse(stream) # this stream convert to python data
        serializer = EmployeeSerializer(data = pythondata) # that python data convert to complex data that is Query set.
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')

