from django.contrib import admin

# Register your models here.
from users.models import CustomUser, Comment



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'avatar_preview')
    list_display_links = ('id','username', 'email', 'first_name', 'last_name')
    search_fields = ('id','username', 'email', 'first_name', 'last_name')


    fieldsets = (
        ('User', {'fields': ('username', 'password', 'email')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar', 'profession', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('avatar_preview',)
 
    def avatar_preview(self,obj):
        if obj.avatar:
            return '<img src="{}" width="50" height="50" />'.format(obj.avatar.url)
        return ""
    
    avatar_preview.allow_tags = True
    avatar_preview.short_description = 'Avatar Preview'



@admin.register(Comment)
class CommentUser(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at')
    list_display_links = ('id', 'user', 'content')
    search_fields = ('id', 'user__username', 'content')
    list_filter = ('created_at',)