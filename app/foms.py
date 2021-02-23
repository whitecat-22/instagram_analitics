from django import forms

class HashtagForm(fomrs.Form):
    hashtag = forms.CharField(max_length=100, label="ハッシュタグ")
    
