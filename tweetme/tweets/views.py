from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tweet
from django.utils import timezone


# Create your views here.
class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()
    model = Tweet
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        id = self.kwargs.get("id")
        # obj = Tweet.objects.get(id=id)  # GET from database
        obj = get_object_or_404(Tweet, id=id)  # GET from database
        return obj


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object": queryset
    }
    return render(request, "tweets/list_view.html", context)


def tweet_detail_view(request, id=None):
    # obj = Tweet.objects.get(id=id)  # GET from database
    obj = get_object_or_404(Tweet, id=id)  # GET from database
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
