from django.urls import path
from . import views


urlpatterns = [
	#path('', views.create_journal_view, name="list_journal"),
	path('create/', views.create_journal_view, name='create_journal'),
	path('view/<int:journal_id>', views.create_journal_view, name='view_journal'),
]