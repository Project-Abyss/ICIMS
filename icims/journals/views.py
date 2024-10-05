from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Journal, Comment
from .forms import JournalForm, CommentForm
from bson import ObjectId
from accounts.models import Data_user, Enterprise, Internship

# Create Journal
def create_journal_view(request):
	user = User.objects.get(username='sheep')
	userId = user.id
	
	internships = Internship.objects.filter(user=userId)
	enterprise_ids = internships.values_list('enterprise', flat=True)
	enterprises = Enterprise.objects.filter(_id__in=enterprise_ids)

	if request.method == 'POST':
		form = JournalForm(request.POST)
		if form.is_valid():
			enterprise_name = form.cleaned_data('enterprise')
			enterprise = get_object_or_404(Enterprise, full_name=enterprise_name)
			title = form.cleaned_data('title')
			content = form.cleaned_data['content']

			journal = Journal.objects.create(
				enterprise=enterprise,
				user=user,
				title=title,
				content=content,
				last_updated=timezone.now()
			)
				
			return redirect('list_journal')
		
		else:
			print("form is invalid")
			print(form.errors)
	else:
		form = JournalForm()


	context = {
		'form': form,
		'enterprises': enterprises,
		'user': user
	}
			
	return render(request, 'create_journal.html', context)
		

# Create Comment <-- Combine with [View Journal] in the future
def view_journal_view(request, journal_id):
	journal = get_object_or_404(Journal, _id=ObjectId(journal_id))
	context = {
		'journal': journal
	}
	return render(request, 'view_journal.html', context)


def list_journal_view(request):
	user = User.objects.get(username='sheep')
	userId = user.id
	
	user_journals = Journal.objects.filter(user_id=userId)
	
	for journal in user_journals:
		journal.id_str = str(journal._id)

	context = {
		'journals': user_journals
	}
	return render(request, 'list_journal.html', context)