from django.urls import path
from . import views
urlpatterns = [
	path('', views.AuditListView.as_view(),name='audits'),
	path('<int:pk>/',views.AuditDetailView.as_view(),name='rules'),
]