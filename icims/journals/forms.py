from django import forms
from django.contrib.auth.models import User
from accounts.models import Enterprise
from .models import Journal, Comment

class JournalForm(forms.ModelForm):
	#for Manual User setting
	user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
	enterprise = forms.ModelChoiceField(queryset=Enterprise.objects.all(), required=True)

	class Meta:
		model = Journal
		fields = ['user', 'enterprise', 'title', 'content']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['user', 'journal', 'content']