from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartForm
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import gettext as _



class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["add_to_cart_form"] = AddToCartForm()
        return context
    

class CommentCreateView(SuccessMessageMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_message = _("Your messages has been sent successfully")

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data
    #     )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return super().form_valid(form)
    