# Generated by Django 4.2.1 on 2023-05-03 18:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateTimeField(default=django.utils.timezone.now)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Tanlangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
        migrations.CreateModel(
            name='SavatItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveIntegerField(default=1)),
                ('yetkazish_sana', models.DateField()),
                ('yetkazish_puli', models.PositiveSmallIntegerField(default=15000)),
                ('umumiy_narx', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('savat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savat_items', to='buyurtma.savat')),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('berilgan_sana', models.DateTimeField(default=django.utils.timezone.now)),
                ('manzil', models.CharField(max_length=255)),
                ('yetkazish_sana', models.DateField()),
                ('summa', models.PositiveIntegerField(blank=True, null=True)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
                ('savat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat')),
            ],
        ),
    ]
