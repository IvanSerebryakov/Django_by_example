from django.contrib.auth.models import User
from django.db.models import (Model,
                              CharField,
                              SlugField,
                              ForeignKey,
                              CASCADE,
                              TextField,
                              DateTimeField)
from django.utils import timezone


class Post(Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = CharField(max_length=250)
    slug = SlugField(max_length=250,
                     unique_for_date='publish')
    author = ForeignKey(User,
                        on_delete=CASCADE,
                        related_name='blog_posts')
    body = TextField()
    publish = DateTimeField(default=timezone.localtime().now())
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    status = CharField(max_length=10,
                       choices=STATUS_CHOICES,
                       default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
