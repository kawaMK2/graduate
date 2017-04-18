from django import forms
from material import Layout, Row


class EditForm(forms.Form):
    first_name = forms.CharField(label='名')
    last_name = forms.CharField(label='性')
    email = forms.EmailField()
    interest = forms.ChoiceField(choices=((None, 'Interested in'), ('D', 'Design'), ('C', 'Development'),
                                          ('I', 'Illustration'), ('B', 'Branding'), ('V', 'Video')))
    budget = forms.ChoiceField(choices=((None, 'Budget'), ('S', 'Less than $5000'), ('M', '$5000-$10000'),
                                        ('L', '$10000-$20000'), ('XL', 'More than $20000')))
    attachment = forms.FileField(label="Include some file...")
    message = forms.CharField(widget=forms.Textarea)

    layout = Layout(Row('last_name', 'first_name'), 'email',
                    Row('interest', 'budget'),
                    'attachment', 'message')
