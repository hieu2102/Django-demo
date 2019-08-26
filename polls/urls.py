from django.urls import path
from . import views

#namespace
app_name = 'polls'

#url list
urlpatterns = [
    path('',views.index, name = 'index'),
    path('details/<int:question_id>',views.detail,name = 'detail'),
    path('details/<int:question_id>/result/', views.results,name = 'results'),
    path('details/<int:question_id>/vote/', views.vote, name = 'vote'),

]