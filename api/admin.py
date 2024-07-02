from django.contrib import admin
from .models import Recruitment, Announcement


@admin.register(Announcement)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    search_fields = ("title",)
    list_filter = ("is_active", "created_at")
    ordering = ("-created_at",)


@admin.register(Recruitment)
class RecruitmentsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "sig_of_interest", "created_at")
    search_fields = ("name", "email", "phone", "sig_of_interest")
    list_filter = ("sig_of_interest", "created_at")
    ordering = ("-created_at",)
