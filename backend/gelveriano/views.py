from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DemandaAlimentos
from .serializers import DemandaAlimentosSerializer


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
