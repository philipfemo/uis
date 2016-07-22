from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'products'
urlpatterns = [
    url(r'^create/$', views.CreateProductView.as_view(), name="product_create"),
    #url(r'^create/$', views.project_create, name="project_create"),
    url(r'^$', views.IndexView.as_view(), name="productslist"),
    url(r'^manage_products/$', views.manage_products, name="products_manage"),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateProductView.as_view(), name="product_edit"),
    url(r'^categories/$', views.CategoryIndexView.as_view(), name="categorieslist"),
    url(r'^categories/create/$', views.CreateCategoryView.as_view(), name="category_create"),
    url(r'^categories/edit/(?P<pk>\d+)/$', views.UpdateCategoryView.as_view(), name="category_edit"),
    url(r'^history/$', views.OperationHistoryView.as_view(), name="product_history" ),
    #url(r'^$', views.projectslist, name="projectslist"),
]
