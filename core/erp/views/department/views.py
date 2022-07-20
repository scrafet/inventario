from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from core.erp.models import Department


# def category_list(request):
#     data = {
#         'title': 'Listado de Categorias',
#         'categories': Category.objects.all
#     }
#     return render(request, 'category/list.html', data)

class DepartmentListView(ListView):
    model = Department
    template_name = 'department/list.html'

    # @method_decorator(login_required) 'solicita login
    # @method_decorator(csrf_exempt)   #quitaMiddleware
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     return redirect('erp:category_list2')
        return super().dispatch(request, *args, **kwargs)

    # @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # print(request.POST)
            data = Department.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = cat.name
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Departamentos'
        context['create_url'] = reverse_lazy('erp:department_create')
        return context
