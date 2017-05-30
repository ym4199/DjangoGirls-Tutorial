from django import forms

class PostCreateForm(forms.Form):
    title = forms.CharField(label ='제목', max_length=10, required=True)
    text = forms.CharField(label='내용', widget=forms.TextInput(attrs={"class":'form-control'}), required=True)
