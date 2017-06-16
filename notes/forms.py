from django import forms
from datetime import datetime
from material import *


class AddForm(forms.Form):
    title = forms.CharField(label="タイトル", max_length=200, required=True)
    content = forms.CharField(label='内容', widget=forms.Textarea(attrs={'cols': '140', 'rows': '20'}), required=True)
    locate = forms.CharField(label='場所', max_length=100, required=True)
    date = forms.DateField(label='日付', initial=datetime.now())
    start_time = forms.DateTimeField(label='開始時刻', initial=datetime.now())
    end_time = forms.DateTimeField(label='終了時刻', initial=datetime.now())
    elapsed_time = forms.IntegerField(label='経過時間')
    text_type = forms.ChoiceField(label='テキストタイプ', choices=((1, 'html'), (2, 'wiki'), (3, 'markdown')))

    layout = Layout('title', Row('locate', 'date'), Row('start_time', 'end_time'), Row('elapsed_time', 'text_type'), 'content')
