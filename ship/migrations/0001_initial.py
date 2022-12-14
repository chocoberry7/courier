# Generated by Django 4.1.1 on 2022-10-13 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senders_country', models.CharField(max_length=50, verbose_name='sender country')),
                ('package', models.CharField(default='3 Items', max_length=10, verbose_name='items')),
                ('status', models.CharField(default='In Transit', max_length=100, verbose_name='status')),
                ('Cargo', models.CharField(max_length=100, verbose_name='type_of_cargo')),
                ('delivery_type', models.CharField(default='Door-To-Door', max_length=50, verbose_name='Delivery Type')),
                ('destinations1', models.CharField(max_length=100, verbose_name='Receivers_country')),
                ('destinations2', models.CharField(max_length=100, verbose_name='Receivers_port')),
                ('destinations3', models.CharField(max_length=100, verbose_name='Receivers_address')),
                ('weight', models.CharField(max_length=100, verbose_name='weight')),
                ('delivery_mode', models.CharField(default='Home Delivery', max_length=100, verbose_name='Delivery mode')),
                ('products', models.CharField(default='Unknown', max_length=100, verbose_name='Product')),
                ('qty', models.CharField(max_length=100, verbose_name='Quantity')),
                ('payment_mode', models.CharField(default='Agent', max_length=100, verbose_name='Payment mode')),
                ('shipment_date', models.DateTimeField(verbose_name='Shipment Date')),
                ('pick_up_date', models.DateTimeField(verbose_name='Pick Up Date')),
                ('reverse_date', models.DateTimeField(verbose_name='Reverse Date')),
                ('parcel', models.CharField(default='Pallet', max_length=100, verbose_name='Parcel')),
                ('Description', models.CharField(default='Carton', max_length=100, verbose_name='Desc')),
                ('length', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='length')),
                ('width', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Width')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Height')),
                ('total_volumetric', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Volumetric')),
                ('actual_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Actual')),
                ('expected_pickup_date', models.DateTimeField(verbose_name='Expected Pick Up Date')),
                ('agents_name', models.CharField(max_length=100, verbose_name='Agent Name')),
                ('freight_charges', models.CharField(max_length=100, verbose_name='Amount')),
                ('freight_total', models.CharField(max_length=100, verbose_name='Freight_total')),
                ('tracking_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ship.trackingid')),
            ],
        ),
        migrations.CreateModel(
            name='SendersInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Senders Name')),
                ('address', models.CharField(max_length=100, verbose_name='Senders Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Senders Phone')),
                ('Email', models.EmailField(max_length=100, verbose_name='Senders Email')),
                ('tracking_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ship.trackingid')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiversInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Receivers Name')),
                ('address', models.CharField(max_length=100, verbose_name='Receivers Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Receivers Phone')),
                ('Email', models.EmailField(max_length=100, verbose_name='Receivers Email')),
                ('Mode_of_transport', models.CharField(default='Unknown', max_length=100, verbose_name='Receivers Mode of Transit')),
                ('Issn', models.CharField(default='Unknown', max_length=100, verbose_name='Receivers')),
                ('tracking_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ship.trackingid')),
            ],
        ),
        migrations.CreateModel(
            name='PackageProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.CharField(max_length=50, verbose_name='confirmed')),
                ('processing', models.CharField(blank=True, max_length=50, verbose_name='processing')),
                ('checked', models.CharField(blank=True, max_length=50, verbose_name='checked')),
                ('delayed', models.CharField(blank=True, max_length=50, verbose_name='delayed')),
                ('dispatched', models.CharField(blank=True, max_length=50, verbose_name='dispatched')),
                ('delivered', models.CharField(blank=True, max_length=50, verbose_name='delivered')),
                ('tracking_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ship.trackingid')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('address', models.CharField(max_length=50, verbose_name='Company Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Company Phone')),
                ('Email', models.EmailField(max_length=100, verbose_name='Company Email')),
                ('mode_of_transport', models.CharField(max_length=100, verbose_name='Mode of Transit')),
                ('Issn', models.CharField(max_length=100, verbose_name='Mode Number')),
                ('tracking_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ship.trackingid')),
            ],
        ),
    ]
