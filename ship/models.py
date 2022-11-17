from django.db import models
from datetime import date


class TrackingId(models.Model):
    name = models.CharField(max_length=42)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField('Company Name', max_length=100)
    address = models.CharField('Company Address', max_length=50)
    phone = models.CharField('Company Phone', max_length=100)
    Email = models.EmailField('Company Email', max_length=100)
    mode_of_transport = models.CharField('Mode of Transit', max_length=100)
    Issn = models.CharField('Mode Number', max_length=100)
    tracking_id = models.ForeignKey(TrackingId, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ReceiversInfo(models.Model):
    name = models.CharField('Receivers Name', max_length=100)
    address = models.CharField('Receivers Address', max_length=100)
    phone = models.CharField('Receivers Phone', max_length=100)
    Email = models.EmailField('Receivers Email', max_length=100)
    Mode_of_transport = models.CharField('Receivers Mode of Transit', default='Unknown', max_length=100)
    Issn = models.CharField('Receivers', default='Unknown', max_length=100)
    tracking_id = models.ForeignKey(TrackingId, default='', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tracking_id)


class SendersInfo(models.Model):
    name = models.CharField('Senders Name', max_length=100)
    address = models.CharField('Senders Address', max_length=100)
    phone = models.CharField('Senders Phone', max_length=100)
    Email = models.EmailField('Senders Email', max_length=100)
    tracking_id = models.ForeignKey(TrackingId, default='', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tracking_id)


class PackageProgress(models.Model):
    confirmed = models.CharField('confirmed', max_length=50, blank=False)
    processing = models.CharField('processing',  max_length=50, blank=True)
    checked = models.CharField('checked', max_length=50, blank=True)
    delayed = models.CharField('delayed',   max_length=50, blank=True)
    dispatched = models.CharField('dispatched',  max_length=50, blank=True)
    delivered = models.CharField('delivered',  max_length=50, blank=True)
    tracking_id = models.ForeignKey(TrackingId, default='', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tracking_id)


class Summary(models.Model):
    tracking_id = models.ForeignKey(TrackingId, default='', on_delete=models.CASCADE)
    senders_country = models.CharField('sender country', max_length=50)
    package = models.CharField('items', default='3 Items', max_length=10)
    status = models.CharField('status', default='In Transit', max_length=100)
    Cargo = models.CharField('type_of_cargo', max_length=100)
    delivery_type = models.CharField('Delivery Type', default='Door-To-Door', max_length=50)
    destinations1 = models.CharField('Receivers_country', max_length=100)
    destinations2 = models.CharField('Receivers_port', max_length=100)
    destinations3 = models.CharField('Receivers_address', max_length=100)
    weight = models.CharField('weight', max_length=100)
    delivery_mode = models.CharField('Delivery mode', default='Home Delivery', max_length=100)
    products = models.CharField('Product', default='Unknown', max_length=100)
    qty = models.CharField('Quantity', max_length=100)
    payment_mode = models.CharField('Payment mode', default='Agent', max_length=100)
    shipment_date = models.DateTimeField('Shipment Date')
    pick_up_date = models.DateTimeField('Pick Up Date')
    reverse_date = models.DateTimeField('Reverse Date')
    parcel = models.CharField('Parcel', default='Pallet', max_length=100)
    Description = models.CharField('Desc', default='Carton', max_length=100)
    length = models.DecimalField('length', max_digits=5, decimal_places=2)
    width = models.DecimalField('Width', max_digits=5, decimal_places=2)
    height = models.DecimalField('Height', max_digits=5, decimal_places=2)
    total_volumetric = models.DecimalField('Volumetric', max_digits=5, decimal_places=2)
    actual_weight = models.DecimalField('Actual', max_digits=5, decimal_places=2)
    expected_pickup_date = models.DateTimeField('Expected Pick Up Date')
    agents_name = models.CharField('Agent Name', max_length=100)
    freight_charges = models.CharField('Amount', max_length=100)
    freight_total = models.CharField('Freight_total', max_length=100)

    def __str__(self):
        return str(self.tracking_id)








