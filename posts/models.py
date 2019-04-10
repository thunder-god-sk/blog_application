from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils.safestring import mark_safe
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from markdown_deux import markdown
from .utils import get_read_time
# This is the Post model it is used as an sql database table and its atributes are its column names


def upload_loaction(instance, filename):
    return "{}/{}".format(instance.id, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=True, default=1)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_loaction,
                              null=True, blank=True, width_field='width_field', height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    read_time = models.TimeField(null = True, blank = True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
# This method get the absolute url of a particular post from the database

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.pk})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
# This class is used to order the mode post in web page

    class Meta:
        ordering = ['-timestamp', '-updated']

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.content:
        html_string = instance.get_markdown()
        time = get_read_time(html_string)
        print(time)
        instance.read_time = time
pre_save.connect(pre_save_post_receiver,sender=Post)

