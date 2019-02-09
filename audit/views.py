from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Audit, Rule, Numeral, Question
from django.urls import reverse_lazy
from django.http import Http404
from .forms import AuditCreateForm, RuleCreateForm, NumeralCreateForm, QuestionCreateForm

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
        numeral = self.get_object()
        last = numeral.pk -1
        next = numeral.pk +1
        try:
            if Numeral.objects.get(pk=last):
                context['last']=last
        except Exception as e:
            pass
        try:
            if Numeral.objects.get(pk=next):
                context['next']=next
        except Exception as e:
            pass
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
        questions = Question.objects.filter(numeral__rule__audit=audit)
        total_questions = len(questions)
        questions_none = len(questions.filter(conflict='none'))
        questions_observation = len(questions.filter(conflict='observation'))
        questions_find = len(questions.filter(conflict='find'))
        questions_none_percent = (questions_none*100)/total_questions
        questions_find_percent = (questions_find*100)/total_questions
        questions_observation_percent = (questions_observation*100)/total_questions
        unanswered_questions = total_questions-(questions_observation+questions_find+questions_none)
        unanswered_percent = (unanswered_questions*100)/total_questions
        context['questions'] = {
            'questions':questions,
            'total':total_questions,
            'observation':questions_observation,
            'find':questions_find,
            'none':questions_none,
            'none_percent':questions_none_percent,
            'find_percent':questions_find_percent,
            'observation_percent':questions_observation_percent,
            'unanswered_questions':unanswered_questions,
            'unanswered_percent':unanswered_percent
        }
        return context

class AuditCreateView(CreateView):
    template_name = "audit/create_audit.html"
    form_class = AuditCreateForm
    success_url = reverse_lazy('audit:audits')

class RuleCreateView(CreateView):
    template_name = "audit/create_rule.html"
    form_class = RuleCreateForm
    success_url = reverse_lazy('audit:audits')

class NumeralCreateView(CreateView):
    template_name = "audit/create_numeral.html"
    form_class = NumeralCreateForm
    success_url = reverse_lazy('audit:audits')

class QuestionCreateView(CreateView):
    template_name = "audit/create_question.html"
    form_class = QuestionCreateForm
    success_url = reverse_lazy('audit:audits')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        numerals = Numeral.objects.all()
        context['numerals']=numerals
        return context