from django.urls import path
from udemy_cbvs import views


app_name='udemy_cbvs'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('create/',views.SchoolCreateView.as_view(),name='create'), 
    path('<pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('delete/<pk>/',views.SchoolDeleteView.as_view(),name='delete'),
    path('update/<pk>/',views.SchoolUpdateView.as_view(),name='update'),
]
