from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FeedbackForms

class main_page(FormView):
    form_class = FeedbackForms
    template_name = 'my_site/index.html'
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
