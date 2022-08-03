from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer, TranscriptionSerializer
from .process import parse
from .models import Transcription
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request):

    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize them 
        serializer = DrinkSerializer(drinks, many=True)
        # return json
        return JsonResponse({"drinks": serializer.data})

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            pass

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response({"drink": serializer.data})  

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def transcription_list(request):
    if request.method == 'GET':
        transcriptions = Transcription.objects.all()
        serializer = TranscriptionSerializer(transcriptions, many=True)
        return JsonResponse({"transcriptions": serializer.data})
    if request.method == 'POST':
        new_data = dict()
        # new_data['id'] = request.data['id']
        new_data['name'] = request.data['name']
        new_data['text'] = request.data['text']
        resp = parse(request.data['text'])
        new_data['temperature'] = resp['temperature']
        new_data['pulse'] = resp['pulse']
        new_data['bp_systolic'] = resp['bp_systolic']
        new_data['bp_diastolic'] = resp['bp_diastolic']
        new_data['discharge'] = resp['discharge']
        new_data['drugs'] = resp['drugs']
        new_data['fhr'] = resp['fhr']
        new_data['dilatation'] = resp['dilatation']
        new_data['effacement'] = resp['effacement']
        
        serializer = TranscriptionSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)