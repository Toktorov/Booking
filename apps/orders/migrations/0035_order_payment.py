# Generated by Django 3.2.7 on 2021-09-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_alter_order_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('в обработке', 'в обработке'), ('принят', 'принят'), ('действительный', 'действительный'), ('недействительный', 'недействительный')], default='в обработке', max_length=255, verbose_name='Cтатус заказа:'),
        ),
    ]