from django import forms
from django.contrib.auth.models import User
from accounts.models import Enterprise
from .models import Journal, Comment

class JournalForm(forms.ModelForm):
	class Meta:
		model = Journal
		fields = ['user', 'enterprise', 'title', 'content']
		labels = {
			'user': '使用者名稱',
			'enterprise': '實習機構',
			'title': '日誌標題',
			'content': '日誌內容',
		}
	enterprise = forms.ChoiceField(choices=[], label="Enterprise")
	title = forms.CharField(max_length=255, label="Title")
	content = forms.CharField(widget=forms.Textarea, label="Content")

	def __init__(self, *args, **kwargs):
		enterprises = kwargs.pop('enterprise', [])
		super().__init__(*args, **kwargs)
		self.fields['enterprise'].choices = [(e.full_name, e.full_name) for e in enterprises]


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['user', 'journal', 'content']