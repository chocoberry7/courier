from django import forms
from django.forms import ModelForm
from .models import Summary, PackageProgress, SendersInfo, ReceiversInfo, ContactInfo


class ContactForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ('name', ' address ', 'phone ', 'email ', 'mode_of_transport', 'issn')
        # bootstrap Event input fields

    labels = {
            'name': 'Enter  Name',
            'address': 'Enter Companies Address',
            'phone': 'Enter Companies phone',
            'email': 'Enter Companies email',
            'mode_of_transport': 'Enter freight mode',
            'issn': 'Enter cargo ref',
     }

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Companies Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Companies Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Companies Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Companies email'}),
            'mode_of_transport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Air Freight'}),
            'issn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Rx28-Ex34'}),
    }


class ReceiversForm(ModelForm):
    class Meta:
        model = ReceiversInfo
        fields = ('name', ' address ', 'phone ', 'email ')
        # bootstrap Event input fields

    labels = {
            'name': 'Receivers Name',
            'address': 'Enter Receivers Address',
            'phone': 'Enter Receivers phone',
            'email': 'Enter Receivers email',

     }

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Receivers Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Receivers Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Receivers Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Receivers email'}),
    }


class SendersForm(ModelForm):
    class Meta:
        model = SendersInfo
        fields = ('name', ' address ', 'phone ', 'email ')
        # bootstrap Event input fields

    labels = {
            'name': 'Senders Name',
            'address': 'Enter Senders Address',
            'phone': 'Enter Senders phone',
            'email': 'Enter Senders email',

     }

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Senders Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Senders Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Senders Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Senders email'}),
    }


class ProgressForm(ModelForm):
    class Meta:
        model = PackageProgress
        fields = ('confirmed', 'processing', 'delayed', 'dispatched', 'delivered')

    labels = {
        'confirmed': 'confirmed',
        'processing': 'processing',
        'delayed': 'delayed',
        'dispatched': 'dispatched',
        'delivered': 'delivered',
    }
    widgets = {
        'confirmed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirmed'}),
        'processing': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'processing'}),
        'delayed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'delayed'}),
        'dispatched': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dispatched'}),
        'delivered': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'delivered'}),
    }


class SummaryForm(ModelForm):
    class Meta:
        model = Summary
        fields = (
            'senders_country',
            'package',
            'status',
            'Cargo',
            'delivery_type',
            'destinations1',
            'destinations2',
            'weight',
            'delivery_mode',
            'track_number',
            'products',
            'qty',
            'payment_mode',
            'shipment_date',
            'pick_up_date',
            'reverse_date',
            'parcel',
            'Description',
            'length',
            'width',
            'height',
            'total_volumetric',
            'actual_weight',
            'expected_pickup_date',
            'agents_name',
            'freight_charges',
            'freight_total',
        )

    labels = {
        'senders_country': 'Enter senders_country',
        'package': 'Enter package',
        'status': 'Enter status',
        'Cargo': 'Enter Cargo',
        'delivery_type': 'Enter delivery_type',
        'destinations1': 'Enter destinations1',
        'destinations2': 'Enter destinations2',
        'weight': 'Enter weight',
        'delivery_mode': 'Enter delivery_mode',
        'track_number': 'Enter track_number',
        'products': 'Enter products',
        'qty': 'Enter qty',
        'payment_mode': 'Enter payment_mode',
        'shipment_date': 'Enter shipment_date',
        'pick_up_date': 'Enter pick_up_date',
        'reverse_date': 'Enter reverse_date',
        'parcel': 'Enter parcel',
        'Description': 'Enter Description',
        'length': 'Enter length',
        'width': 'Enter width',
        'height': 'Enter height',
        'total_volumetric': 'Enter total_volumetric',
        'actual_weight': 'Enter actual_weight',
        'expected_pickup_date': 'Enter expected_pickup_date',
        'agents_name': 'Enter agents_name',
        'freight_charges': 'Enter freight_charges',
        'freight_total': 'Enter freight_total',
    }
    widgets = {
        'senders_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter senders_country'}),
        'package': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: 3 Items'}),
        'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : In Transit'}),
        'Cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg Ocean Freight'}),
        'delivery_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : Door-To-Door'}),
        'destinations1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: Spain'}),
        'destinations2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: Taiyuan Seaport'}),
        'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : 15kg '}),
        'delivery_mode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : Home Delivery'}),
        'track_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : NPR2-W8CF-1235' }),
        'products': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: Unknown'}),
        'qty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: 4 '}),
        'payment_mode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : agent'}),
        'shipment_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : 2022-02-23'}),
        'pick_up_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : 2022-03-08'}),
        'reverse_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : 2022-03-22'}),
        'parcel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : Pallet'}),
        'Description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : Cartons'}),
        'length': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg 40cm'}),
        'width': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: 28cm'}),
        'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : 32cm'}),
        'total_volumetric': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg:Length*Width*height'}),
        'actual_weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: 9kg'}),
        'expected_pickup_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: 2022-03-02'}),
        'agents_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg : Mrs Sarah'}),
        'freight_charges': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: $970'}),
        'freight_total': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: + insurance  $1045 '}),
    }





