from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

	PAYMENT_METHOD_CHOICES = (
		('Ví Momo', 'Ví Momo'),
		('Thẻ ngân hàng','Thẻ ngân hàng'),
		('Thanh toán trực tiếp', 'Thanh toán trực tiếp'),
	)

	#division = forms.ChoiceField(choices=DIVISION_CHOICES)
	#district = forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'payment_method']
