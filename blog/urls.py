from django.urls import path

# views
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='home_blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    # 
    path('contact/', views.contact_view, name='contact'),

    
] 