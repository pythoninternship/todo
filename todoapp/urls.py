
from . import views
from django.urls import path


urlpatterns = [

    path('',views.todo,name='todo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupadte'),
    path('cbvdelete.<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]
