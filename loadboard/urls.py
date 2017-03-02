#this is the url page that holds all urls for the loadboard section
#planning for various urls user can navigate to from the loadboard area

from django.conf.urls import url
from . import views

#this specifies which url page to look at from the html pages
app_name = 'loadboard'

urlpatterns = [
    # /loadboard/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /loadboard/71/
    #Note: the ?P below is basically how you use pass parameter of company_table_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /loadboard/loadboarditem/add/
    url(r'loadboarditem/add/$', views.LoadboardCreate.as_view(), name='loadboarditem-add')

]