from django.conf.urls import urls
from blog import views

urlpatterns = [

url(r'^about/$',views.AboutView.as_view(),name='about'),
url(r'^$',views.PostListView.as_view(),name="post_list"),


]


