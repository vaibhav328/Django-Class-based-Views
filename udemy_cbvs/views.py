from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from . import models
# Create your views here.

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('class based views are cool!')
    
class IndexView(TemplateView):
    template_name='index.html'
    
    # kwarge key word arguements
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['injectme']='BASIC INJECTION'
        return context
    

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    #  returns school_list
    
    
class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    # returns school
    template_name='udemy_cbvs/school_detail.html'
    
class SchoolCreateView(CreateView):
    fields= ('name','principal','location')
    model=models.School
    
class SchoolUpdateView(UpdateView):
    fields= '__all__'
    model=models.School
    
class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('udemy_cbvs:list')


