from django.urls import path
from . import views


urlpatterns = [
	path('', views.list_journal_view, name="list_journal"),
	path('create/', views.create_journal_view, name='create_journal'),
	path('view/<str:journal_id>/', views.view_journal_view, name='view_journal'),
]