#from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from advert.models import Advert
from advert.serializers import AdvertSerializer


@api_view(['GET', 'POST'])
def advert_list(request):
    """
    List all snippets, or create a new article.
    """

    if request.method == 'GET':
        advert1 = Advert.objects.all()
        serializer=AdvertSerializer(advert1, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def advert_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        advert2 = Advert.objects.get(pk=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertSerializer(advert2)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertSerializer(advert2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        advert2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.




# Create your views here.
