from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from list.views import ArticleListView
from dayArchiveView.views import ArticleDayArchiveView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('article-list/', ArticleListView.as_view()),
    path('<int:year>/<str:month>/<int:day>/',
         ArticleDayArchiveView.as_view(),
         name="archive_day"),
]