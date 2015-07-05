from django import forms
from AGEs.models import Item, Picture

class PersonForm(forms.ModelForm):
    item_name = forms.CharField(max_length=128, help_text="Please enter the person name.")
    num_of_pictures = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Item
        # TODO: このfieldsがいまいち何のためか理解できていない
        fields = ('item_name',)
        
class PictureForm(forms.ModelForm): 
    picture_name = forms.CharField(max_length=64, help_text="Please enter the picture name.")
    age = forms.IntegerField(help_text="Please enter the person age.") 
    description = forms.CharField(max_length=200, help_text="Please enter the picture description.")
    
    class Meta:
        model = Picture
        fields = ('picture_name', 'age', 'description', 'image',)
        
class PersonSearchForm(forms.ModelForm):
    item_name = forms.CharField(max_length=128)
    class Meta:
        model = Item
        fields = ('item_name',)
