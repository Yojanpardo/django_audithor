from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Audit, Rule, Numeral, Question

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

class RuleDetailView(DetailView):
    model = Rule
    template_name = "audit/numerals.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        numerals = Numeral.objects.filter(rule=self.get_object())
        context['numerals'] = numerals
        return context

class NumeralDetailView(DetailView):
    model = Numeral
    template_name = "audit/questions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(numeral = self.get_object())
        context['questions'] = questions
        return context