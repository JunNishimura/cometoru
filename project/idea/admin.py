from django.contrib import admin
from .models import PostIdea, RequiredSkill, Comment

# Register your models here.
admin.site.register(PostIdea)
admin.site.register(RequiredSkill)
admin.site.register(Comment)