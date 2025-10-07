
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
            path('', views.render_about_me),
            path('projects/', views.render_projects),
            path('test/', views.test_response),
            path('admin/', admin.site.urls)
            ]


