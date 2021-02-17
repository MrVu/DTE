from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import University, Level, Subject, City, Article, \
    Scholarship, PageInfo, UniSubject, Banner, CustomerComment, CompanyAddress, Tag
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


class LevelInline(admin.TabularInline):
    model = Level


class ScholarshipInline(admin.TabularInline):
    model = Scholarship


class UniSubjectInline(admin.TabularInline):
    model = UniSubject


class UniversityAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ['universityName']
    ordering = ['universityName']
    inlines = [LevelInline, ScholarshipInline]
    filter_horizontal = ('subjects', 'cities', 'uni_subjects')
    readonly_fields = ['slug']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectName']
    inlines = [UniSubjectInline]


class BannerAdmin(ImageCroppingMixin, admin.TabularInline):
    model = Banner


class CustomerCommentAdmin(ImageCroppingMixin, admin.TabularInline):
    model = CustomerComment


class CompanyAddressAdmin(admin.TabularInline):
    model = CompanyAddress


class PageInfoAdmin(admin.ModelAdmin):
    inlines = [BannerAdmin, CustomerCommentAdmin, CompanyAddressAdmin]


class TagAdmin(admin.TabularInline):
    model = Tag


class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [TagAdmin]
    readonly_fields = ['slug']


# admin.site.register(Level)
# admin.site.register(Tracking, TrackingAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(City)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PageInfo, PageInfoAdmin)
