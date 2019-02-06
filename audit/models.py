from django.db import models

# Create your models here.

class Audit(models.Model):
	"""este es el modelo que almacenará los datos mas generales de la auditoria"""
	auditor_name = models.CharField(max_length=50)
	audited_name = models.CharField(max_length=50)
	audited_job = models.CharField(max_length=255)
	process_to_be_audited = models.CharField(max_length=100)
	audit_scope = models.CharField(max_length=255)
	audited_phone_number = models.CharField(max_length=15)
	date = models.DateField()

	#metadata

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.process_to_be_audited

class Rule(models.Model):
	audit = models.OneToOneField(Audit, on_delete=models.CASCADE)
	rule_name = models.CharField(max_length=50)
	rule_title = models.CharField(max_length=100)

	#metadata

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.rule_name
 	
class Numeral(models.Model):
	rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
	numeral = models.CharField(max_length=8)
	title = models.CharField(max_length=255)

	#metadata

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}) {}'.format(self.numeral,self.title)

class Question(models.Model):
	CONFLICTS = (
		('none','Ninguno'),
		('observation','Observación'),
		('find','Hallazgo'),
	)

	numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
	question = models.CharField(max_length=255)
	method = models.TextField(max_length=255, blank=True,null=True)
	conflict = models.CharField(max_length=11, choices=CONFLICTS, blank=True, null=True)
	conflict_description = models.TextField(blank=True,null=True)
	evidence = models.ImageField(upload_to='evidences',blank=True,null=True)

	#metadata

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question