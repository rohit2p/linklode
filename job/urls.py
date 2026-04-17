from django.urls import path

from joblink.job import admin
from . import views

app_name = 'job'

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/<int:pk>/download/', views.resource_download, name='resource_download'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]