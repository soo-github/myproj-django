# Generated by Django 3.2.11 on 2022-01-13 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=100, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('[ㄱ-힣]', message='한글을 한 글자 이상 입력해주세요.')])),
                ('poster', models.ImageField(blank=True, upload_to='')),
                ('story', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]