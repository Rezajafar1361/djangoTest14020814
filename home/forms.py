from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField(label='عنوان')
    body = forms.CharField(label='توضیحات')
    created = forms.DateTimeField(label='زمان ثبت')

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'