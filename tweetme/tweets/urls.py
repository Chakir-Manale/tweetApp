from .views import *
from django.urls import path, include

urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path(r'', TweetListView.as_view(), name='list'),
    path(r'tweet-<int:id>', TweetDetailView.as_view(), name='detail'),
    path(r'', tweet_create_view, name='create'),
    path(r'', tweet_update_view, name='update'),
    path(r'', tweet_delete_view, name='delete'),
]
