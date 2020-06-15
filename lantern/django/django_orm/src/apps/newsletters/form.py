from django.forms import ModelForm

from apps.newsletters.models import Newsletter


class NewslettersForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
