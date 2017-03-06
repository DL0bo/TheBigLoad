from django.views import generic
from .models import Company_table, Loadboard_table


class IndexView(generic.ListView):
    template_name = 'loadboard/index.html' # the variable contains which html file this view should point to
    context_object_name = 'all_loadboard' # this variable contains the items from the 'get_queryset(self)' function

    def get_queryset(self):
        return Loadboard_table.objects.all() # queries a list into variable 'context_object_name' variable above

class DetailView(generic.DetailView):
    model = Company_table
    template_name = 'loadboard/detail.html'


class LoadboardCreate(generic.CreateView):
    model = Loadboard_table
    fields = ['Origin', 'Destination', 'Company', 'Email']


