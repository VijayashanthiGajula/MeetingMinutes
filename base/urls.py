from django.urls import path
from .views  import ActionCreate, ActionList,ActionDetail, ActionUpdate, DeleteView,CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns =[   
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', ActionList.as_view(), name='actions'),
    path('action/<int:pk>/', ActionDetail.as_view(), name='action'),
    path('action-create/', ActionCreate.as_view(), name='action-create'),
    path('action-update/<int:pk>/', ActionUpdate.as_view(), name='action-update'),
      path('action-delete/<int:pk>/', DeleteView.as_view(), name='action-delete'),
     #path('',views.ActionsList,name='Actions')
]