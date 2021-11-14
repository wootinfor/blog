from django.contrib import admin
from django.db.models import fields

from article.models import Article,Users,ModelWithFileField, userComment
class UserAdmin(admin.ModelAdmin):
    list_display=('username','password')
    list_filter=('username','password')
    search_fields=('username','password')
class ArticleAdmin(admin.ModelAdmin):
    fields=('title','content',)
    list_display=('title','short_content','publish_date','user')
    list_filter=('title',)
    search_fields=('title',)
    
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        super().save_model(request, obj, form, change)

# admin.site.register(Users,UserAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(ModelWithFileField)
admin.site.register(userComment)
# Register your models here.
