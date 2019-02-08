from django.urls import path
from . import views
urlpatterns = [
	path('', views.AuditListView.as_view(),name='audits'),
	path('<int:pk>/',views.AuditDetailView.as_view(),name='rules'),
	path('detail/<int:pk>/',views.AuditRankingView.as_view(),name='detail'),
	path('<int:audit_pk>/<int:pk>/',views.RuleDetailView.as_view(),name='numerals'),
	path('<int:audit_pk>/<int:rule_pk>/<int:pk>/',views.NumeralDetailView.as_view(),name='questions'),
	path('<int:audit_pk>/<int:rule_pk>/<int:numeral_pk>/<int:pk>',views.QuestionUpdateView.as_view(),name='question'),	
]