# Generated by Django 5.0.4 on 2024-04-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20240415_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'Military Personnel'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='firstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastName',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='nickName',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='joined',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='rank',
            field=models.CharField(default='Alokas', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='resigned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(blank=True, null=True),
        ),
    ]
