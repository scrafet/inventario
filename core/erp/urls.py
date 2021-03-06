from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.department.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('department/list/', DepartmentListView.as_view(), name='department_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('department/add/', DepartmentCreateView.as_view(), name='department_create')
    # path('category/list/', CategoryListView.as_view(), name='category_list'),
    # path('category/list2/', category_list, name='category_list2'),
    # path('category/add/', CategoryCreateView.as_view(), name='category_create'),
]
