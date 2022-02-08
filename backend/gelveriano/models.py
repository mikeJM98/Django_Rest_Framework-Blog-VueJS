from django.db import models

# Create your models here.

class DemandaAlimentos(models.Model):
	distrito = models.CharField(max_length=250)

	nombreDemandante = models.CharField(max_length=250)
	documentoDemandante = models.CharField(max_length=250)
	gradoInstruccionDemandante = models.CharField(max_length=250)
	residenciaDemandante = models.CharField(max_length=250)
	estadoCivilDemandante = models.CharField(max_length=250)
	domicilioProcesalDemandante = models.CharField(max_length=250)

	nombreSolicitante1 = models.CharField(max_length=250)
	edadSolicitante1 = models.CharField(max_length=250)
	vinculo1 = models.CharField(max_length=250)
	discapacidad1 = models.CharField(max_length=250)
	detalleDiscapacidad1= models.CharField(max_length=250)
	nombreSolicitante2 = models.CharField(max_length=250)
	edadSolicitante2 = models.CharField(max_length=250)
	vinculo2 = models.CharField(max_length=250)
	discapacidad1 = models.CharField(max_length=250)
	detalleDiscapacidad1= models.CharField(max_length=250)

	nombreDemandado = models.CharField(max_length=250)
	documentoDemandado = models.CharField(max_length=250)
	gradoInstruccionDemandado = models.CharField(max_length=250)
	residenciaDemandado = models.CharField(max_length=250)
	estadoCivilDemandado = models.CharField(max_length=250)
	domicilioNotificarDemandado = models.CharField(max_length=250)

	fijacionAlimentos = models.CharField(max_length=250)
	montoPension = models.CharField(max_length=250)
	asignacionAnticipadaAlimento = models.CharField(max_length=250)
	montoAsignacionAnticipada = models.CharField(max_length=250)

	fundamentoDemanda = models.CharField(max_length=250)

	necesidadesComestibles = models.CharField(max_length=250)
	montoNecesidadesComestibles = models.CharField(max_length=250)
	necesidadesVivienda = models.CharField(max_length=250)
	montoNecesidadesVivienda = models.CharField(max_length=250)
	necesidadesVestimenta = models.CharField(max_length=250)
	montoNecesidadesVestimenta = models.CharField(max_length=250)
	necesidadesEducacion = models.CharField(max_length=250)
	montoNecesidadesEducacion = models.CharField(max_length=250)
	necesidadesMedicas = models.CharField(max_length=250)
	montoNecesidadesMedicas = models.CharField(max_length=250)
	necesidadesRecreacion = models.CharField(max_length=250)
	montoNecesidadesRecreacion = models.CharField(max_length=250)
	otrasNecesidades = models.CharField(max_length=250)

	dependenciaLaboral = models.CharField(max_length=250)
	empresaLaboral = models.CharField(max_length=250)
	actividadesDedica = models.CharField(max_length=250)
	ingresosMensuales = models.CharField(max_length=250)
	informacionAdicional = models.CharField(max_length=250)
	otrosHijosDelDemandado = models.CharField(max_length=250)


class HijosDelDemandado(models.Model):
	nombre = models.CharField(max_length=250)
	edad = models.CharField(max_length=250)
	demanda = models.ForeignKey(DemandaAlimentos, on_delete=models.CASCADE, related_name='demandaAlimentos')