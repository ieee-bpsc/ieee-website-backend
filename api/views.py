from rest_framework import viewsets, generics
from .serializers import AnnouncementSerializer, RecruitmentSerializer
from .models import Announcement, Recruitment
from .mixins import CSRFExemptMixin


class AnnouncementsListView(CSRFExemptMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer


class RecruitmentsCreateView(CSRFExemptMixin, generics.CreateAPIView):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer
