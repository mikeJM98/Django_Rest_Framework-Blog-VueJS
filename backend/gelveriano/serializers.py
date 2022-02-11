from rest_framework import serializers
from .models import DemandaAlimentos

class DemandaAlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemandaAlimentos
        fields = (
            'distrito' ,

            'nombreDemandante' ,
            'documentoDemandante' ,
            'gradoInstruccionDemandante' ,
            'residenciaDemandante' ,
            'estadoCivilDemandante' ,
            'domicilioProcesalDemandante' ,

            'nombreSolicitante1' ,
            'edadSolicitante1' ,
            'vinculo1' ,
            'discapacidad1' ,
            'detalleDiscapacidad1' ,
            'nombreSolicitante2' ,
            'edadSolicitante2' ,
            'vinculo2' ,
            'discapacidad2' ,
            'detalleDiscapacidad2' ,

            'nombreDemandado' ,
            'documentoDemandado' ,
            'gradoInstruccionDemandado' ,
            'residenciaDemandado' ,
            'estadoCivilDemandado' ,
            'domicilioNotificarDemandado' ,

            'fijacionAlimentos' ,
            'montoPension' ,
            'montoPensionPorcentaje' ,
            'asignacionAnticipadaAlimento' ,
            'montoAsignacionAnticipada' ,
            'montoAsignacionAnticipadaPorcentaje' ,

            'fundamentoDemanda' ,

            'necesidadesComestibles' ,
            'montoNecesidadesComestibles' ,
            'necesidadesVivienda' ,
            'montoNecesidadesVivienda' ,
            'necesidadesVestimenta' ,
            'montoNecesidadesVestimenta' ,
            'necesidadesEducacion' ,
            'montoNecesidadesEducacion' ,
            'necesidadesMedicas' ,
            'montoNecesidadesMedicas' ,
            'necesidadesRecreacion' ,
            'montoNecesidadesRecreacion' ,
            'otrasNecesidades' ,

            'dependenciaLaboral' ,
            'empresaLaboral' ,
            'actividadesDedica' ,
            'ingresosMensuales' ,
            'informacionAdicional' ,
            'otrosHijosDelDemandado' ,

            'mediosProbatorios' ,
        )