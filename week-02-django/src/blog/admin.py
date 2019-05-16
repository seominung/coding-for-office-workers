from django.contrib import admin
from .models import Article, Comment
# Register your models here.
@admin.register(Article, Comment) # 대문자 구분 잘 해라
class BlogAdmin(admin.ModelAdmin):
    pass
