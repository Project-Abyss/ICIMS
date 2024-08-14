from django.contrib import admin

from journals.models import Journal, Comment


# Register your models here.
class JournalAdmin(admin.ModelAdmin):
    list_display = ('_id', 'title', 'user', 'enterprise', 'last_updated', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('_id', 'journal', 'last_updated', 'content')


admin.site.register(Journal, JournalAdmin)
admin.site.register(Comment, CommentAdmin)