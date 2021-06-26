from django import forms  
from EList.models import Item  
class DiaryForm(forms.ModelForm):  
	class Meta:  
		model = Item 
		fields = "__all__"  