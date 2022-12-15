from django.urls import path
from . import views
app_name='newapp'
urlpatterns = [
    path('',views.fun1,name='fun1'),
    path('novel/<int:x_id>/',views.details,name='details'),
    path('add/',views.add_novels,name='add_novels'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]