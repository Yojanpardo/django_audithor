from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Audit, Rule, Numeral, Question
from django.urls import reverse_lazy
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

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = "audit/question.html"
    fields = ['question','method','conflict','conflict_description','evidence']

    def get_success_url(self):
    	question = self.get_object()
    	audit = Audit.objects.get(pk=question.numeral.rule.audit.pk)
    	rule = Rule.objects.get(pk=question.numeral.rule.pk)
    	numeral = Numeral.objects.get(pk=question.numeral.pk)
    	return reverse_lazy('audit:questions', kwargs={
    		'audit_pk':audit.pk,
    		'rule_pk':rule.pk,
    		'pk':numeral.pk
    		})

class AuditRankingView(DetailView):
	model = Audit
	template_name = "audit/ranking.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		audit = self.get_object()
		rules = Rule.objects.filter(audit=audit)
		numerals = Numeral.objects.filter(rule=rules)
		questions = Question.objects.filter(numeral=numeral)
		context['questions'] = questions
		return context