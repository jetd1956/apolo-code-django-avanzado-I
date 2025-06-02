from django.views.generic import TemplateView

from core.pos.models import Company


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.first()
        context['logo'] = company.get_image()
        return self.render_to_response(context)


