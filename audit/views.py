from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Audit, Rule

# Create your views here.

class AuditListView(ListView):
    model = Audit
    template_name = "audit/audits.html"
    context_object_name = 'audits'

class AuditDetailView(DetailView):
    model = Audit
    template_name = "audit/rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rules = Rule.objects.filter(audit=self.get_object())
        context['rules'] = rules
        return context