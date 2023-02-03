from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .utils import *


class HomeView(DataMixin, ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        return dict(list(super().get_context_data(**kwargs).items()) + list(self.get_user_context().items()))

    def get_queryset(self):
        return Article.objects.all().order_by('-time_created')

# def index(request):
#     articles = Article.objects.all().order_by('-time_created')
#
#     context = {
#         'categories': categories,
#         'articles': articles,
#     }
#     return render(request, 'articles/index.html', context=context)


class ArticleView(DataMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = dict(list(super().get_context_data(**kwargs).items()) + list(self.get_user_context().items()))
        # cat = context['article'].category_id
        return context

# def show_article(request, article_slug):
#     article = Article.objects.get(slug=article_slug)
#
#     context = {
#         'categories': categories,
#         'article': article,
#     }
#     return render(request, 'articles/article.html', context=context)


class CategoryView(DataMixin, ListView):
    model = Article
    template_name = 'articles/category.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = dict(list(context.items()) +
                       list(self.get_user_context(cat=context['articles'][0].category).items()))
        return context

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug']).order_by('-time_created')

# def show_category(request, category_slug):
#     cat = get_object_or_404(Category, slug=category_slug)
#
#     articles = Article.objects.filter(category=cat).order_by('-time_created')
#
#     context = {
#         'cat': cat,
#         'categories': categories,
#         'articles': articles,
#     }
#     return render(request, 'articles/category.html', context=context)


class CreateArticleView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'articles/addarticle.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        return dict(list(super().get_context_data(**kwargs).items()) + list(self.get_user_context().items()))


# def add_article(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'form': form,
#         'categories': categories,
#     }
#
#     return render(request, 'articles/addarticle.html',  context=context)



