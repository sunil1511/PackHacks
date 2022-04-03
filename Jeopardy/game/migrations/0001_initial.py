# Generated by Django 4.0.3 on 2022-04-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('QID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('answers', models.CharField(max_length=500)),
                ('question_word', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.question')),
            ],
            options={
                'db_table': 'Topic',
            },
        ),
    ]
