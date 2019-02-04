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
