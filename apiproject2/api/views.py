
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from . models import Student
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def get_student(request):
       students=Student.objects.all()
       serializers=StudentSerializer(students,many=True)
       return Response(serializers.data)

@api_view(["POST"])
def add_student(request):
       serializers=StudentSerializer(data=request.data)
       if serializers.is_valid():
              serializers.save()
              return Response(serializers.data,status=201)
       
@api_view(['PUT'])
def fully_update(request,pk):
       student=Student.objects.get(id=pk)
       serializers=StudentSerializer(student,data=request.data)

       if serializers.is_valid():
              serializers.save()
              return Response(serializers.data)
              

       return Response(serializers.errors)

@api_view(['PATCH'])
def partially_add(request,pk):
       student=Student.objects.get(id=pk)
       serializers=StudentSerializer(student,data=request.data, partial=True)

       if serializers.is_valid():
              serializers.save()
              return Response(serializers.data)
       return Response(serializers.errors)

@api_view(['DELETE'])
def delete_student(request,pk):
       student=Student.objects.get(id=pk)
       student.delete()
       return Response("message deleted")