from django.urls import path

from . import views
urlpatterns = [
    path('<int:year>',views.display),
    path('',views.display),
    path('more/<int:id>',views.all),
]