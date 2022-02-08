from rest_framework import serializers
from .models import DemandaAlimentos

class DemandaAlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemandaAlimentos
        fields = (
            'id',
            'distrito',
            'nombreDemandante',
            'documentoDemandante',
            'gradoInstruccionDemandante',
            'residenciaDemandante',
            'estadoCivilDemandante',
            'domicilioProcesalDemandante',
        )