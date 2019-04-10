from urllib import parse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm
from django.db.models import Q

from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm
# This View is used to create the post
# @param request This is common for all views and is used because in
# web we use request to do almost every thing like http Get Request and post request
# this method use the form that is created in forms.py to form a post and then save it
# if it is valid


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    form = PostForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    elif request.method == 'POST':
        messages.error(request, "Some thing wrong happen try again later")
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

# this view is used for the detail view of the post


def post_detail(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    share_string = parse.quote_plus(instance.content)
    comments = instance.comments
    # initial data for the comment form
    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }
    # creating and instantiating the Comment Form Object and giving it initial data to create the comment for a particular post
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        # if the form is valid the getting the content_type from the comment_form
        # getting the object id from the comment_form
        # getting the content from the comment_form
        # form that data from form creating the whole comment (Comment model)
        c_type = comment_form.cleaned_data.get('content_type')
        obj_id = comment_form.cleaned_data.get('object_id')
        content_type = ContentType.objects.get(model=c_type)
        content_data = comment_form.cleaned_data.get('content')
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            comentText=content_data,
            parent=parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    context = {
        'instance': instance,
        'share_string': share_string,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)
# This is the main view where a list of blog posts is showed to the user


def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 4)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    query = request.GET.get('q')
    if query:
        queryset = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query)

        )
    context = {
        'posts': queryset
    }
    return render(request, 'post_list.html', context)
# This view is used to update the content of certain post
# it takes id and request as a parameter id to determine which post to enit


def post_update(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "successfully updated")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            form = PostForm(instance=instance)
            context = {
                'title': instance.title,
                'instance': instance,
                'form': form,
            }
            messages.error(request, "Something went wrong")
            return render(request, 'post_form.html', context)
    else:
        form = PostForm(instance=instance)
        context = {
            'title': instance.title,
            'instance': instance,
            'form': form,
        }
    return render(request, 'post_form.html', context)
# As the name suggest this is used to delete the post with the provided id


def post_delete(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    if request.method == "POST" and request.user == instance.user:
        instance.delete()
        messages.success(request, 'post has been deleted successfully ')
        return redirect('posts:post-list')
    return render(request, 'confirm_delete.html', {'object': instance})
