# Generated by Django 2.2.5 on 2019-10-01 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('child_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_fn', models.CharField(max_length=20, verbose_name='Parent First Name')),
                ('parent_ln', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('profession', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_in_school', models.CharField(choices=[('NUR', 'Nursery'), ('PG', 'Play Group'), ('LKG', 'Lower KinderGarten'), ('UKG', 'Upper KinderGarten')], default='NUR', max_length=20)),
                ('child_relationship', models.ManyToManyField(through='homepage.Child', to='homepage.Parent')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='child_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Parent'),
        ),
        migrations.AddField(
            model_name='child',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Grades'),
        ),
    ]
