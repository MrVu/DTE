from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import SaleSummary, Customer, Tracking, University, Level, Subject, GuestCustomer, City, Article, \
    Scholarship, PageInfo
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User as MyUser
from image_cropping import ImageCroppingMixin

User_model = get_user_model()


@admin.register(User_model)
class UserAdmin(OrigUserAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'username', 'email', 'is_active')
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    fieldsets = OrigUserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')}),
    )  # this will allow to change these fields in admin module


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['fullName']
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class TrackingAdmin(admin.ModelAdmin):
    list_display = ['userName', 'request', 'date']


class LevelInline(admin.TabularInline):
    model = Level


class ScholarshipInline(admin.TabularInline):
    model = Scholarship


class UniversityAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ['universityName']
    inlines = [LevelInline, ScholarshipInline]
    filter_horizontal = ('subjects', 'cities',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectName']


class GuestCustomerAdmin(admin.ModelAdmin):
    search_fields = ['guest_name']
    list_display = ['guest_name', 'email', 'phone_number']


# admin.site.register(Level)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tracking, TrackingAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(GuestCustomer, GuestCustomerAdmin)
admin.site.register(City)
admin.site.register(Article)
admin.site.register(PageInfo)
