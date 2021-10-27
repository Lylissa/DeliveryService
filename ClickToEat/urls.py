from django.urls impport path
from . import views

 

app_name = 'ClickToEat'
urlpatterns = [

 

path('home',views.homepage_view.as_view(), name="ClickToEat_home_view"),
#path('dashboard',views.DashboardIndexView.as_view(), name="dashboard_view"),

]