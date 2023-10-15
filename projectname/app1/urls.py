from django.urls import path


from . import views


urlpatterns = [
  path("",views.index, name ="index"),
  path("remark",views.display, name="display"),
  path("exemple/<str:parameter>", views.exemple_view, name="exemple"),
]