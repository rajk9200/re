from django import forms
from .models import Posts
class PostForm(forms.ModelForm):
    class Meta:
        model =Posts
        fields =['title', 'name','sort_info', 'desc']

    sort_info =forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    desc =forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'