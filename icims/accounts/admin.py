from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from accounts.models import Data_user, Enterprise, Internship


# Register your models here.
class DataUserInline(admin.StackedInline):
    model = Data_user
    can_delete = False
    verbose_name_plural = 'Data_User'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (DataUserInline, )

    list_display = ("username", "get_fullname", "get_role", "is_staff", "is_superuser", "date_joined")
    list_select_related = ("data_user", )

    ordering = ["username"]

    def get_role(self, instance):
        return instance.data_user.role
    get_role.short_description = 'Role'

    def get_fullname(self, instance):
    	return instance.data_user.full_name
    get_fullname.short_description = 'Full Name'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class DataUserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_id', 'full_name', 'role', 'email', 'department', 'phone')

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('_id', 'full_name', 'address', 'telephone')

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user', 'enterprise', 'academic_year', 'start_date', 'end_date')



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Data_user, DataUserAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Internship, InternshipAdmin)