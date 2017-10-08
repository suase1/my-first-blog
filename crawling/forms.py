from django.forms import ModelForm
from crawling.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields=['name','title','contents','url','email']
        
