# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Blog, UserProfile, BlogComment, Item, Cart ,ItemComment

from pagedown.widgets import AdminPagedownWidget
from django.db import models


# Register your models here.
admin.site.register(Blog)
#admin.site.register(Author)
admin.site.register(UserProfile)
admin.site.register(BlogComment)
admin.site.register(ItemComment)
admin.site.register(Item)
admin.site.register(Cart)


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }