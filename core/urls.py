from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "IEEE Website Admin"
admin.site.site_title = "IEEE Website Admin Portal"
admin.site.index_title = "Welcome to the IEEE Website Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
