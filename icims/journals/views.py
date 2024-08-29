from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Journal, Comment
from .forms import JournalForm, CommentForm

from accounts.models import Data_user, Enterprise, Internship

# Create Journal
def create_journal_view(request):
	if request.method == 'POST':
		form = JournalForm(request.POST)
		if form.is_valid():
		# Get data from form
			#user = request.user #Auto grap present user
			user = form.cleaned_data('user')

			enterprise_name = form.cleaned_data('enterprise')
			enterprise = get_object_or_404(Enterprise, full_name=enterprise_name)
			title = form.cleaned_data('title')
			content = form.cleaned_data['content']

			journal = Journal.objects.create(
				enterprise=enterprise,
				user=user,
				title=title,
				content=content)

			return redirect('homepage') #Should go to journal_list.html
	else:
		form = JournalForm()
	return render(request, 'create_journal.html', {'form':form})

# Create Comment <-- Combine with [View Journal] in the feture
def view_journal_view(request, journal_id):
	journal - Journal.objects.get(id=journal_id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_vaild():
			commen = form.save (comment = False)
			comment.journal = journal
			comment.save()
			return redirect('homepage')#Should go to [Original journal].html
	else:
		form = CommentForm()

	comments = Comment.objects.filter(journal = journal)
	return render(request, 'journals/view_journal.html', {
		'journal': journal,
		'form': form,
		'comments': comments,
	})
