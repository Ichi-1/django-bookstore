from django.urls import path

from .views import HomePageView, ProductByCategoryListView, ProductDetailView

app_name = "store"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "categories/<slug:category_slug>",
        ProductByCategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "categories/<slug:category_slug>/<slug:slug>",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
]
