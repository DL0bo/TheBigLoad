from django.views import generic
from .models import Company_table, Loadboard_table


class IndexView(generic.ListView):
    template_name = 'loadboard/index.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return Company_table.objects.all()



class DetailView(generic.DetailView):
    model = Company_table
    template_name = 'loadboard/detail.html'


class LoadboardCreate(generic.CreateView):
    model = Loadboard_table
    fields = ['Origin', 'Destination', 'Company', 'Email']


