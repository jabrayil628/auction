# Generated by Django 2.2.6 on 2019-11-14 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('identification', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('social_account', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
