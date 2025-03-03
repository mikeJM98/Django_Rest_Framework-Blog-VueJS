# Generated by Django 3.2.6 on 2022-02-09 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gelveriano', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandaalimentos',
            name='detalleDiscapacidad2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='demandaalimentos',
            name='discapacidad2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='demandaalimentos',
            name='mediosProbatorios',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='demandaalimentos',
            name='montoAsignacionAnticipadaPorcentaje',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='demandaalimentos',
            name='montoPensionPorcentaje',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='actividadesDedica',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='asignacionAnticipadaAlimento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='dependenciaLaboral',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='detalleDiscapacidad1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='discapacidad1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='distrito',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='documentoDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='documentoDemandante',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='domicilioNotificarDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='domicilioProcesalDemandante',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='edadSolicitante1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='edadSolicitante2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='empresaLaboral',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='estadoCivilDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='estadoCivilDemandante',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='fijacionAlimentos',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='fundamentoDemanda',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='gradoInstruccionDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='gradoInstruccionDemandante',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='informacionAdicional',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='ingresosMensuales',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoAsignacionAnticipada',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoNecesidadesComestibles',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoNecesidadesEducacion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoNecesidadesMedicas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoNecesidadesRecreacion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoNecesidadesVestimenta',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoNecesidadesVivienda',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='montoPension',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='necesidadesComestibles',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='necesidadesEducacion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='necesidadesMedicas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='necesidadesRecreacion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='necesidadesVestimenta',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='necesidadesVivienda',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='nombreDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='nombreDemandante',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='nombreSolicitante1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='nombreSolicitante2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='otrasNecesidades',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='otrosHijosDelDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='residenciaDemandado',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='residenciaDemandante',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='vinculo1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demandaalimentos',
            name='vinculo2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hijosdeldemandado',
            name='edad',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hijosdeldemandado',
            name='nombre',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
