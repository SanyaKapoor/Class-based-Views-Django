from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from list.views import ArticleListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('^article-list/', ArticleListView.as_view()),
]