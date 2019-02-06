from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Audit)
class AuditAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Rule)
class RuleAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Numeral)
class NumeralAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
	pass
