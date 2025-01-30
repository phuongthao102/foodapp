
from django.contrib import admin
from django import forms
from django.template.response import TemplateResponse
from .models import Store, FoodItem, Food, Lesson, Tag
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from food import dao





class FoodAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống'
    index_title = "Chào mừng đến với quản trị"

    def get_urls(self):
        return [
            path('food-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': dao.count_food_by_cate()
        })

admin_site = FoodAppAdminSite(name='myapp')


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'food_type', 'store']
    search_fields = ['pk', 'name']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_filter = ['name']
    search_fields = ['name']


class FoodForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Food
        fields = '__all__'


class TagInlineAdmin(admin.StackedInline):
    model = Food.tags.through


class FoodAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'store', 'updated_date', 'img', 'active']
    readonly_fields = ['img']
    inlines = [TagInlineAdmin]
    form = FoodForm
    search_fields = ['name']

    def img(self, food):
        if food.image:  # Sử dụng đúng tên trường
            return mark_safe(
                '<img src="{url}" width="120" />'.format(url=food.image.url)
            )
        return "No Image"

    img.short_description = 'Image Preview'

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }
        js = ('/static/js/script.js',)


admin_site.register(Store, StoreAdmin)
admin_site.register(FoodItem, FoodItemAdmin)
admin_site.register(Food,FoodAdmin)
admin_site.register(Lesson)
admin_site.register(Tag)