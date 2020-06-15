from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from apps.newsletters.form import NewslettersForm


class NewsletterView(FormView):
    template_name = 'newsletter.html'
    form_class = NewslettersForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
