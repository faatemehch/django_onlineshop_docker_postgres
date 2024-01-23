from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return super().form_valid(form)
    