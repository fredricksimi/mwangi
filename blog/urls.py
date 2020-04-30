from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>', views.post_detail, name='details'),
    path('create', views.post_create_view, name='create'),
    path('update/<int:id>', views.post_update_view, name='update'),
    path('delete/<int:id>', views.post_delete_view, name='delete'),
]
