# Generated by Django 3.2.5 on 2021-12-09 06:13

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('desc', models.TextField(max_length=500, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('joining_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('sell_price', models.CharField(max_length=200, null=True)),
                ('buy_price', models.CharField(max_length=200, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('in_stock', models.CharField(max_length=200, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('shelf_no', models.CharField(max_length=50, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.company')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField()),
                ('salary_amount', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]