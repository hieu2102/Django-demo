from django.urls import path
from . import views

#namespace
app_name = 'polls'

#url list
urlpatterns = [
    #path('',views.index, name = 'index'),
    #path('details/<int:question_id>',views.detail,name = 'detail'),
    #path('details/<int:question_id>/result/', views.results,name = 'results'),
    #path('details/<int:question_id>/vote/', views.vote, name = 'vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('details/<int:pk>', views.DetailView.as_view(), name='details'),
    path('details/<int:pk>/results', views.ResultsView.as_view(), name= 'results'),
    path('details/<int:question_id>/vote/', views.vote, name = 'vote'),

]