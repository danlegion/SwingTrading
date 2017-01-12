from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.Swing.as_view())

]
