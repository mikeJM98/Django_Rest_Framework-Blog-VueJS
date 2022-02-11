from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status

from .models import DemandaAlimentos
from .serializers import DemandaAlimentosSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = DemandaAlimentosSerializer(data=request.data)
    # validating for already existing data
    if DemandaAlimentos.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
    item = DemandaAlimentos.objects.get(pk=pk)
    data = DemandaAlimentosSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(DemandaAlimentos, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

class DemandaAlimentosListtView(APIView):
    def get(self, request, *args, **kwargs):
        posts = DemandaAlimentos.objects.all()
        serializer = DemandaAlimentosSerializer(posts,many=True)
        return Response(serializer.data)

class DemandaAlimentoView(APIView):
    def get(self, request, id,*args, **kwargs):
        post = get_object_or_404(DemandaAlimentos, id=id)
        serializer = DemandaAlimentosSerializer(post)
        return Response(serializer.data)
