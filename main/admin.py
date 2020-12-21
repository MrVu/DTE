from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import SaleSummary, Customer, JobAvailable, Tracking
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User as MyUser
User_model = get_user_model()


@admin.register(User_model)
class UserAdmin(OrigUserAdmin):
    list_display = (
    'id', 'first_name', 'last_name', 'username', 'email', 'is_active')
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    fieldsets = OrigUserAdmin.fieldsets + (
            (None, {'fields': ('bio', 'birth_date', 'phoneNumber', 'position', 'address','profilePic')}),
    ) #this will allow to change these fields in admin module

class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    def changelist_view(self, request, extra_context=None):
        users = User.objects.all()
        extra_context = extra_context or {}
        extra_context['users'] = users
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        return response

class JobAvailableAdmin(admin.ModelAdmin):
    search_fields= ['position']

class CustomerAdmin(admin.ModelAdmin):
    search_fields= ['fullName']
class TrackingAdmin(admin.ModelAdmin):
    list_display = ['userName', 'request','date']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(JobAvailable,JobAvailableAdmin)
admin.site.register(Tracking, TrackingAdmin)
