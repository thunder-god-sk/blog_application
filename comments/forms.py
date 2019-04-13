from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
class CommentForm(forms.Form):
    content_type = forms.CharField(widget= forms.HiddenInput)
    object_id = forms.CharField(widget = forms.HiddenInput)
    # parent_id = forms.CharField(widget = forms.HiddenInput,required = False)
    content = forms.CharField(label='',widget = forms.Textarea)

