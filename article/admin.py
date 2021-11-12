from django.contrib import admin
from django.db.models import fields

from article.models import Article,Users,ModelWithFileField
class UserAdmin(admin.ModelAdmin):
    list_display=('username','password')
    list_filter=('username','password')
    search_fields=('username','password')
class ArticleAdmin(admin.ModelAdmin):
    fields=('title','content','publish_date','user')
    list_display=('title','short_content','publish_date')
    list_filter=('title',)
    search_fields=('title',)
admin.site.register(Users,UserAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(ModelWithFileField)
# Register your models here.
