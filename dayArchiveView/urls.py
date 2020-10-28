from django.urls import path

from dayArchiveView.views import ArticleDayArchiveView

urlpatterns = [
    # Example: /2012/nov/10/
    path('<int:year>/<str:month>/<int:day>/',
         ArticleDayArchiveView.as_view(),
         name="archive_day"),
]