from django.contrib import admin
from suggest.models import myUser, Post, Comment, Lover
admin.site.register(myUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Lover)

# Register your models here.
