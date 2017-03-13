from django.views import generic
from django.shortcuts import render
from .models import Company_table, Loadboard_table
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'loadboard/index.html'  # the variable contains which html file this view should point to
    context_object_name = 'all_loadboard'  # this variable contains the items from the 'get_queryset(self)' function

    def get_queryset(self):
        return Loadboard_table.objects.all()  # queries a list into variable 'context_object_name' variable above

def ViewCompanyDetails(request, companyId):
    CompanyObject = Company_table.objects.get(id=companyId)
    context = {'Company': CompanyObject,}
    return render(request, 'loadboard/detail.html', context)


class CompanyCreate(CreateView):
    model = Company_table
    fields = ['CompanyName', 'Address', 'CreditScore', 'CompanyLogo']


