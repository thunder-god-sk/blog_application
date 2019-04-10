[1mdiff --git a/src/comments/__pycache__/models.cpython-36.pyc b/src/comments/__pycache__/models.cpython-36.pyc[m
[1mindex 7723db5..ba7d81b 100644[m
Binary files a/src/comments/__pycache__/models.cpython-36.pyc and b/src/comments/__pycache__/models.cpython-36.pyc differ
[1mdiff --git a/src/comments/__pycache__/urls.cpython-36.pyc b/src/comments/__pycache__/urls.cpython-36.pyc[m
[1mindex 42f7201..e2e31ad 100644[m
Binary files a/src/comments/__pycache__/urls.cpython-36.pyc and b/src/comments/__pycache__/urls.cpython-36.pyc differ
[1mdiff --git a/src/comments/__pycache__/views.cpython-36.pyc b/src/comments/__pycache__/views.cpython-36.pyc[m
[1mindex be18db4..7e3bc9f 100644[m
Binary files a/src/comments/__pycache__/views.cpython-36.pyc and b/src/comments/__pycache__/views.cpython-36.pyc differ
[1mdiff --git a/src/comments/models.py b/src/comments/models.py[m
[1mindex 836f39b..6f9df5c 100644[m
[1m--- a/src/comments/models.py[m
[1m+++ b/src/comments/models.py[m
[36m@@ -2,7 +2,7 @@[m [mfrom django.db import models[m
 from django.conf import settings[m
 from django.contrib.contenttypes.fields import GenericForeignKey[m
 from django.contrib.contenttypes.models import ContentType[m
[31m-from django.urls import reverse[m
[32m+[m
 class CommentManager(models.Manager):[m
     def all(self):[m
         qs = super(CommentManager,self).filter(parent = None)[m
[36m@@ -27,11 +27,8 @@[m [mclass Comment(models.Model):[m
         return str(self.user.username)[m
     class Meta:[m
         ordering = ['-timestamp'][m
[31m-    def get_absolute_url(self):[m
[31m-        return reverse('comments:thread',kwargs={'id':self.object_id})[m
     def childrens(self):[m
         return Comment.objects.filter(parent = self)[m
[31m-    [m
     @property[m
     def isParent(self):[m
         if self.parent is not None:[m
[1mdiff --git a/src/comments/urls.py b/src/comments/urls.py[m
[1mindex faaf34d..6277981 100644[m
[1m--- a/src/comments/urls.py[m
[1m+++ b/src/comments/urls.py[m
[36m@@ -19,6 +19,6 @@[m [mfrom .views import comment_thread[m
 app_name = 'comment'[m
 [m
 urlpatterns = [[m
[31m-    path('<int:id>/',comment_thread, name='thread'),[m
[32m+[m[32m    path('<int:abc>/',comment_thread, name='thread'),[m
     # path('<int:pk>/delete', views.post_delete, name='post-delete'),[m
 ][m
\ No newline at end of file[m
[1mdiff --git a/src/comments/views.py b/src/comments/views.py[m
[1mindex 854a0e7..a331d49 100644[m
[1m--- a/src/comments/views.py[m
[1m+++ b/src/comments/views.py[m
[36m@@ -1,21 +1,17 @@[m
 from django.shortcuts import render[m
[31m-from django.shortcuts import get_object_or_404,redirect[m
[32m+[m[32mfrom django.shortcuts import get_object_or_404[m
 from .models import Comment[m
 from django.contrib.contenttypes.models import ContentType[m
 from django.http import HttpResponseRedirect[m
 from .forms import CommentForm[m
[31m-from posts.models import Post[m
 # Create your views here.[m
[31m-def comment_thread(request,id):[m
[31m-    obj = get_object_or_404(Comment, id = id)[m
[31m-    content_object = obj.content_object[m
[31m-    content_id = obj.content_object.id[m
[32m+[m[32mdef comment_thread(request,abc):[m
[32m+[m[32m    obj = get_object_or_404(Comment, id = abc)[m
     initial_data = {[m
[31m-        'content_type':obj.content_type,[m
[31m-        'object_id':content_id[m
[32m+[m[32m        'content_type':[m
[32m+[m[32m        ''[m
     }[m
[31m-    comment_form = CommentForm(request.POST or None, initial =initial_data)[m
[31m-    print(comment_form.errors)[m
[32m+[m[32m    comment_form = CommentForm(request.POST or None)[m
     if comment_form.is_valid():[m
         # if the form is valid the getting the content_type from the comment_form[m
         # getting the object id from the comment_form[m
[36m@@ -42,7 +38,6 @@[m [mdef comment_thread(request,id):[m
             comentText=content_data,[m
             parent = parent_obj[m
             )[m
[31m-        return redirect('thread')[m
     context = {[m
         'comment':obj,[m
         'comment_form':comment_form,[m
[1mdiff --git a/src/db.sqlite3 b/src/db.sqlite3[m
[1mindex 59f9f39..41532d2 100644[m
Binary files a/src/db.sqlite3 and b/src/db.sqlite3 differ
[1mdiff --git a/src/posts/__pycache__/models.cpython-36.pyc b/src/posts/__pycache__/models.cpython-36.pyc[m
[1mindex 390967a..0103133 100644[m
Binary files a/src/posts/__pycache__/models.cpython-36.pyc and b/src/posts/__pycache__/models.cpython-36.pyc differ
[1mdiff --git a/src/posts/__pycache__/urls.cpython-36.pyc b/src/posts/__pycache__/urls.cpython-36.pyc[m
[1mindex c9ddb99..751d3c2 100644[m
Binary files a/src/posts/__pycache__/urls.cpython-36.pyc and b/src/posts/__pycache__/urls.cpython-36.pyc differ
[1mdiff --git a/src/posts/__pycache__/views.cpython-36.pyc b/src/posts/__pycache__/views.cpython-36.pyc[m
[1mindex 2659f48..5fabb47 100644[m
Binary files a/src/posts/__pycache__/views.cpython-36.pyc and b/src/posts/__pycache__/views.cpython-36.pyc differ
[1mdiff --git a/src/posts/urls.py b/src/posts/urls.py[m
[1mindex 79b2ff8..4ec06a0 100644[m
[1m--- a/src/posts/urls.py[m
[1m+++ b/src/posts/urls.py[m
[36m@@ -16,7 +16,6 @@[m [mIncluding another URLconf[m
 from django.contrib import admin[m
 from django.urls import path, include[m
 from . import views[m
[31m-app_name = 'posts'[m
 urlpatterns = [[m
     path('', views.post_list, name='post-list'),[m
     path('new/', views.post_create, name='post-create'),[m
[1mdiff --git a/src/posts/views.py b/src/posts/views.py[m
[1mindex b372759..21c6b33 100644[m
[1m--- a/src/posts/views.py[m
[1m+++ b/src/posts/views.py[m
[36m@@ -14,7 +14,7 @@[m [mfrom comments.forms import CommentForm[m
 # This View is used to create the post[m
 # @param request This is common for all views and is used because in[m
 # web we use request to do almost every thing like http Get Request and post request[m
[31m-# this method use the form that is created in forms.py to form a post and then save it[m
[32m+[m[32m# this method use the form  that is created in forms.py to form a post and then save it[m
 # if it is valid[m
 [m
 [m
[36m@@ -77,7 +77,7 @@[m [mdef post_detail(request, pk=None):[m
             comentText=content_data,[m
             parent = parent_obj[m
             )[m
[31m-        return redirect('post-detail')[m
[32m+[m[32m        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())[m
     context = {[m
         'instance': instance,[m
         'share_string': share_string,[m
[1mdiff --git a/src/templates/post_detail.html b/src/templates/post_detail.html[m
[1mindex 2a9b627..c541c8f 100644[m
[1m--- a/src/templates/post_detail.html[m
[1m+++ b/src/templates/post_detail.html[m
[36m@@ -54,9 +54,7 @@[m
         <blockquote class="blockquote">{{comment.comentText }}[m
         <footer class="blockquote-footer">via {{ comment.user }}| {{comment.timestamp|timesince }} ago [m
           {% if comment.childrens.count > 0 %} {{ comment.childrens.count }} Comments | {% endif %}[m
[31m-          <a class="comment-reply-btn" href="#">Reply</a> |[m
[31m-          <a  href="{{ comment.get_absolute_url }}">Thread</a>  [m
[31m-        </footer>[m
[32m+[m[32m          <a class="comment-reply-btn" href="#">Reply</a> </footer>[m
         <div class="comment-reply" style="display: none">[m
           {% for child_comment in comment.childrens %}[m
           <blockquote class="blockquote">{{child_comment.comentText }}[m
[1mdiff --git a/src/web_blog/__pycache__/urls.cpython-36.pyc b/src/web_blog/__pycache__/urls.cpython-36.pyc[m
[1mindex cced800..a107da7 100644[m
Binary files a/src/web_blog/__pycache__/urls.cpython-36.pyc and b/src/web_blog/__pycache__/urls.cpython-36.pyc differ
[1mdiff --git a/src/web_blog/urls.py b/src/web_blog/urls.py[m
[1mindex 475b5b1..b7e54e2 100644[m
[1m--- a/src/web_blog/urls.py[m
[1m+++ b/src/web_blog/urls.py[m
[36m@@ -19,8 +19,8 @@[m [mfrom django.conf import settings[m
 from django.conf.urls.static import static[m
 urlpatterns = [[m
     path('admin/', admin.site.urls),[m
[31m-    path('posts/', include('posts.urls',namespace = 'posts')),[m
[31m-    path('comments/', include('comments.urls',namespace = 'comments')),[m
[32m+[m[32m    path('posts/', include('posts.urls')),[m
[32m+[m[32m    path('comments/', include('comments.urls')),[m
 ][m
 if settings.DEBUG:[m
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)[m
