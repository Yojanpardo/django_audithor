from django import forms
from . import models 

class AuditCreateForm(forms.ModelForm):
	class Meta:
		model = models.Audit
		fields = [
			'auditor_name',
			'audited_name',
			'audited_job',
			'process_to_be_audited',
			'audit_scope',
			'audited_phone_number',
			'date'
		]

class RuleCreateForm(forms.ModelForm):
	"""docstring for RuleCreateForm"""
	class Meta:
		model = models.Rule
		fields = [
			'audit',
			'rule_name',
			'rule_title'
		]

class NumeralCreateForm(forms.ModelForm):
	class Meta:
		model = models.Numeral
		fields = [
			'rule',
			'numeral',
			'title'
		]

class QuestionCreateForm(forms.ModelForm):
	"""docstring for QuestionCreateForm"""
	class Meta:
		model = models.Question
		fields = [
			'numeral',
			'question'
		]