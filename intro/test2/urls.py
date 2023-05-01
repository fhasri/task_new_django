from django.urls import path 
from .views import get , task_create, task_detail, task_delate, task_update

urlpatterns = [ 
    path('vse_ludi/', get),
    path('all_info/', task_detail),
    path('create_person/', task_create),
    path('delete_person/', task_delate),
    path('update_person/', task_update),

]


