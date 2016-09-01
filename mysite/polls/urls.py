from django.conf.urls import url
from . import views

urlpatterns = [
url(r'b$',views.ReactTestB.as_view()),
url(r'a$',views.ReactTest.as_view()),
url(r'c$',views.ReactTestC.as_view()),
url(r'^$',views.index, name='list')

]
