from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import TemplateView

from core.models import Consulta
from core.forms import ConsultaForm

# Create your views here.
class ConsultaView(TemplateView):

    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('detalle')
    template_name = 'core/formulario_consulta.html'

    def get_context_data(self, **kwargs):
        context = super(ConsultaView, self).get_context_data(**kwargs)
        
        if 'form' not in context:
            context["form"] = self.form_class(self.request.GET) 
        
        return context
    
    def get_success_url(self):
        nombre = self.request.POST.get('nombre_cliente')
        apellido = self.request.POST.get('apellido_cliente')
        slug = slugify(nombre + " " + apellido)
        
        return reverse_lazy('detalle', kwargs={'slug': slug})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
	