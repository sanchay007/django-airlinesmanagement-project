from django.conf.urls import url
from first import views

app_name='first'


urlpatterns=[
	url(r'^$',views.home,name='home'),
	url(r'^flights/',views.flights,name='flights'),
	url(r'^welcome/',views.welcome,name='welcome'),
	url(r'^search/',views.search,name='search'),
]