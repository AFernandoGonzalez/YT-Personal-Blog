from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator

from .forms import ContactForm
from .models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.all()
    post = Post.objects.all()[:1]

    paginator = Paginator(posts, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'post': post,
        'page_obj': page_obj,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }

    return render(request, 'blog/blog_detail.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'blog/email_success.html')

    form = ContactForm()
    context = {
        'form': form
        }
    return render(request, 'blog/contact.html', context)