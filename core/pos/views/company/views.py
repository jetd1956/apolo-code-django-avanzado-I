from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from fontTools.otlLib.optimize import compact

from core.pos.forms import CompanyForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.pos.models import Company


class CompanyUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/create.html'
    success_url = reverse_lazy('dashboard')
    permission_required = 'change_company'
    #url_redirect = success_url    no es necesario

    # sobreescribo este metodo porque el metodo update normal espera el id del registro
    # a actualizar pero en este caso ya sabemos que es 1 y para no quemarlo en la url
    # lo cargamos en este metodo.
    def get_object(self, queryset=None):
        company = Company.objects.all()
        if company.exists():  # si la compañia existe develve el objeto en la 1ra posicion (0)
            return company[0]
        return Company()      # sino devuelve un objeto vacio

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                instance = self.get_object() # obtiene la instancia del objeto a editar
                if instance.pk is not None:  # si existe lo editamos sino creamos
                    form = CompanyForm(request.POST, request.FILES, instance=instance)
                    data = form.save()
                else:
                    form = CompanyForm(request.POST, request.FILES)
                    data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de mi Compañia'
        context['entity'] = 'Compañia'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
