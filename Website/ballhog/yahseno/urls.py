from django.urls  import path
from . import views

urlpatterns = [
    path("", views.index,name='index'),
    path("two/", views.two, name="two"),
    path("three/", views.three, name="three"),
    path("four/", views.four, name="four"),
    path("five/", views.five, name="five"),
    path("six/", views.six, name="six"),


]