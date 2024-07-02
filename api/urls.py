from django.urls import path
from .views import RecruitmentsCreateView, AnnouncementsListView

urlpatterns = [
    path("announcements/", AnnouncementsListView.as_view({"get": "list"})),
    path("recruitments/", RecruitmentsCreateView.as_view()),
]
