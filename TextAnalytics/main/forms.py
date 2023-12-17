from django import forms
from django.forms import widgets


class TextInp(forms.Form):
    inp_text = forms.CharField(
        widget=widgets.Textarea(
            attrs={
                'placeholder': "Введите текст",
                'id': 'inputField'
            }
        ),
        label=''
    )

    inp_sent_count = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={
                'id': 'sent_count',
                'class': 'sent_count'
            }
        ),
        label='',
        min_value=1,
        max_value=15,
        initial=5
    )

