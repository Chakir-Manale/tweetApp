from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .models import Tweet
from django.utils import timezone
from .forms import TweetModelForm
from django import forms
from django.forms.utils import ErrorList
from .mixins import *
from django.contrib.auth.mixins import LoginRequiredMixin


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


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    #  queryset = Tweet.objects.all()
    template_name = "tweets/create_view.html"
    success_url = reverse_lazy('list')
    """
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(TweetCreateView, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in!"])
            return self.form_invalid(form)
    """


class TweetUpdateView(UserOwnerMixin, FormUserNeededMixin, UpdateView):
    form_class = TweetModelForm
    #  queryset = Tweet.objects.all()
    template_name = "tweets/update_view.html"
    success_url = reverse_lazy('list')

    def get_object(self):
        print(self.kwargs)
        id = self.kwargs.get("id")
        print(id)
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
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

    context = {
        "form": form
    }
    return render(request, "tweets/create_view.html", context)


def tweet_delete_view(request):
    context = {

    }
    return render(request, "tweets/detail_view.html", context)


def tweet_update_view(request):
    context = {

    }
    return render(request, "tweets/detail_view.html", context)
