from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0039_inboundfeelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localsettings',
            name='key',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
        ),
    ]
