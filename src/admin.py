from django.contrib import admin
from .models import User, BLog , CategoryBlog, Comment
# Register your models here.


admin.site.register(User)
admin.site.register(BLog)
admin.site.register(CategoryBlog)
admin.site.register(Comment)
