from django.urls import path
from core.erp.views.category.views import category_list

app_name = 'erp'

urlpatterns = [
    path('category/list/', category_list, name='category_list')
    # path('category/list/', CategoryListView.as_view(), name='category_list'),
    # path('category/list2/', category_list, name='category_list2'),
    # path('category/add/', CategoryCreateView.as_view(), name='category_create'),
]
