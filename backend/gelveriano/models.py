from django.db import models

# Create your models here.

class DemandaAlimentos(models.Model):
	distrito = models.CharField(max_length=250,blank=True, null=True)

	nombreDemandante = models.CharField(max_length=250,blank=True, null=True)
	documentoDemandante = models.CharField(max_length=250,blank=True, null=True)
	gradoInstruccionDemandante = models.CharField(max_length=250,blank=True, null=True)
	residenciaDemandante = models.CharField(max_length=250,blank=True, null=True)
	estadoCivilDemandante = models.CharField(max_length=250,blank=True, null=True)
	domicilioProcesalDemandante = models.CharField(max_length=250,blank=True, null=True)

	nombreSolicitante1 = models.CharField(max_length=250,blank=True, null=True)
	edadSolicitante1 = models.CharField(max_length=250,blank=True, null=True)
	vinculo1 = models.CharField(max_length=250,blank=True, null=True)
	discapacidad1 = models.CharField(max_length=250,blank=True, null=True)
	detalleDiscapacidad1= models.CharField(max_length=250,blank=True, null=True)
	nombreSolicitante2 = models.CharField(max_length=250,blank=True, null=True)
	edadSolicitante2 = models.CharField(max_length=250,blank=True, null=True)
	vinculo2 = models.CharField(max_length=250,blank=True, null=True)
	discapacidad2 = models.CharField(max_length=250,blank=True, null=True)
	detalleDiscapacidad2= models.CharField(max_length=250,blank=True, null=True)

	nombreDemandado = models.CharField(max_length=250,blank=True, null=True)
	documentoDemandado = models.CharField(max_length=250,blank=True, null=True)
	gradoInstruccionDemandado = models.CharField(max_length=250,blank=True, null=True)
	residenciaDemandado = models.CharField(max_length=250,blank=True, null=True)
	estadoCivilDemandado = models.CharField(max_length=250,blank=True, null=True)
	domicilioNotificarDemandado = models.CharField(max_length=250,blank=True, null=True)

	fijacionAlimentos = models.CharField(max_length=250,blank=True, null=True)
	montoPension = models.CharField(max_length=250,blank=True, null=True)
	montoPensionPorcentaje = models.CharField(max_length=250,blank=True, null=True)
	asignacionAnticipadaAlimento = models.CharField(max_length=250,blank=True, null=True)
	montoAsignacionAnticipada = models.CharField(max_length=250,blank=True, null=True)
	montoAsignacionAnticipadaPorcentaje = models.CharField(max_length=250,blank=True, null=True)

	fundamentoDemanda = models.CharField(max_length=250,blank=True, null=True)

	necesidadesComestibles = models.CharField(max_length=250,blank=True, null=True)
	montoNecesidadesComestibles = models.CharField(max_length=250,blank=True, null=True)
	necesidadesVivienda = models.CharField(max_length=250,blank=True, null=True)
	montoNecesidadesVivienda = models.CharField(max_length=250,blank=True, null=True)
	necesidadesVestimenta = models.CharField(max_length=250,blank=True, null=True)
	montoNecesidadesVestimenta = models.CharField(max_length=250,blank=True, null=True)
	necesidadesEducacion = models.CharField(max_length=250,blank=True, null=True)
	montoNecesidadesEducacion = models.CharField(max_length=250,blank=True, null=True)
	necesidadesMedicas = models.CharField(max_length=250,blank=True, null=True)
	montoNecesidadesMedicas = models.CharField(max_length=250,blank=True, null=True)
	necesidadesRecreacion = models.CharField(max_length=250,blank=True, null=True)
	montoNecesidadesRecreacion = models.CharField(max_length=250,blank=True, null=True)
	otrasNecesidades = models.CharField(max_length=250,blank=True, null=True)

	dependenciaLaboral = models.CharField(max_length=250,blank=True, null=True)
	empresaLaboral = models.CharField(max_length=250,blank=True, null=True)
	actividadesDedica = models.CharField(max_length=250,blank=True, null=True)
	ingresosMensuales = models.CharField(max_length=250,blank=True, null=True)
	informacionAdicional = models.CharField(max_length=250,blank=True, null=True)
	otrosHijosDelDemandado = models.CharField(max_length=250,blank=True, null=True)

	mediosProbatorios = models.CharField(max_length=250,blank=True, null=True)


class HijosDelDemandado(models.Model):
	nombre = models.CharField(max_length=250,blank=True, null=True)
	edad = models.CharField(max_length=250,blank=True, null=True)
	demanda = models.ForeignKey(DemandaAlimentos, on_delete=models.CASCADE, related_name='demandaAlimentos')