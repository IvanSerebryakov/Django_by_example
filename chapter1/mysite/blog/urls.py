from django.urls import path

from chapter1.mysite.blog import views

app_name = 'chapter1.mysite.blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail')
]