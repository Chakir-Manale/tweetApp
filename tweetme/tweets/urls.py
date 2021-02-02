from .views import *
from django.urls import path


urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path(r'', tweet_list_view, name='list'),
    path(r'', tweet_detail_view, name='detail'),
    path(r'', tweet_create_view, name='create'),
    path(r'', tweet_update_view, name='update'),
    path(r'', tweet_delete_view, name='delete'),
]
