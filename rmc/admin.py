from django.contrib import admin
from rmc.models import User, Session, Professional
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class Users (admin.ModelAdmin):
    model = User
    list_display = ('id','user_name', 'name', 'email','is_active')
    list_display_links = ('id','user_name', 'name', 'email','is_active')
    list_per_page: 20

admin.site.register(User, Users)

class Professionals(admin.ModelAdmin):
    list_display = ('id', 'name','user_name', 'email','specialization','is_active')
    list_display_links = ('id',)
    search_fields = ('specialization',)
    list_filter = ('email', 'user_name', 'is_active')
    list_per_page = 20

admin.site.register(Professional, Professionals)

class Sessions(admin.ModelAdmin):
    list_display = ('id', 'user', 'professional', 'data', 'num_session', 'payment')
    list_display_links = ('id',)

admin.site.register(Session, Sessions)

