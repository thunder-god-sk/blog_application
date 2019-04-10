from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect,Http404
from .forms import CommentForm
from posts.models import Post
from django.contrib import messages
# View for the confirmation of delete of the comment 
def comment_delete(request, id = None):
    instance = None
    try:
        instance = Comment.objects.get(id = id)
    except:
        raise Http404
    if instance.user == request.user:    
        if request.method=='POST':
            parent_obj_url = instance.content_object.get_absolute_url()
            instance.delete()
            messages.success(request,"Successfully deleted")
            return HttpResponseRedirect(parent_obj_url)
    else:
        raise Http404
    context ={
        'object':instance
    }
    return render(request,'confirm_delete.html',context)

def comment_thread(request,id):
    obj = get_object_or_404(Comment, id = id)
    content_object = obj.content_object
    content_id = obj.content_object.id
    initial_data = {
        'content_type':obj.content_type,
        'object_id':content_id
    }
    comment_form = CommentForm(request.POST or None, initial =initial_data)
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
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
       
        new_comment,created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            comentText=content_data,
            parent = parent_obj
            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    context = {
        'comment':obj,
        'comment_form':comment_form,
    }
    return render(request,'comment_thread.html',context)
