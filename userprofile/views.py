from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all snippets, or create a new article.
    """

    if request.method == 'GET':
        userprofile1 = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofile1, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        user1 = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



