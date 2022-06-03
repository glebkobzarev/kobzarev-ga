from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
<<<<<<< HEAD
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]

=======
 # post views
 path('', views.post_list, name='post_list'),
 path('<int:id>/', views.post_detail, name='post_detail'),
]
>>>>>>> 761f8fac9ce22fdea80e4ba390301800017b8f42
