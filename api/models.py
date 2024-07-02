from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_active = models.BooleanField(default=True, verbose_name="Is Active?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Recruitment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    about = models.TextField()
    sig_of_interest = models.CharField(max_length=100, verbose_name="SIG of Interest")
    github_url = models.URLField(verbose_name="GitHub URL")
    linkedin_url = models.URLField(verbose_name="LinkedIn URL")
    other_comments = models.TextField(verbose_name="Other Comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.sig_of_interest
