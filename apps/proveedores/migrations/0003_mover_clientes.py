from django.db import migrations


def mover_clientes(apps, schema_editor):
    ClienteAnterior = apps.get_model('proveedores', 'Clientes')
    ClienteNuevo = apps.get_model('clientes', 'Clientes')

    ClienteNuevo.objects.bulk_create(
        ClienteNuevo(
            id=cliente.id,
            name=cliente.name,
            last_name=cliente.last_name,
            tipo_usuario=cliente.tipo_usuario,
        )
        for cliente in ClienteAnterior.objects.all()
    )


class Migration(migrations.Migration):
    dependencies = [
        ('clientes', '0001_initial'),
        ('proveedores', '0002_proveedor'),
    ]

    operations = [
        migrations.RunPython(mover_clientes, migrations.RunPython.noop),
        migrations.DeleteModel(name='Clientes'),
    ]
