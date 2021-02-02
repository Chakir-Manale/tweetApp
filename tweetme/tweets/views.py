from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self, queryset=None):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()


# Create your views here.
def tweet_list_view(request):
    queryset = Tweet.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object": queryset
    }
    return render(request, "tweets/list_view.html", context)


def tweet_detail_view(request):
    obj = Tweet.objects.get(id=id)  # GET from database
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_create_view(request):
    return render(request, "tweets/detail_view.html", {})


def tweet_delete_view(request):
    return render(request, "tweets/detail_view.html", {})


def tweet_update_view(request):
    return render(request, "tweets/detail_view.html", {})
