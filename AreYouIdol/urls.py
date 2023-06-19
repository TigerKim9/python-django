from django.urls import path
from . import views

from django.conf.urls import(
    handler400,handler500,handler404,handler403
)
urlpatterns = [
    path('', views.find),
    path('result/',views.resultIdol)
]

# handler403 = 
# handler404 = 
# handler400 = 
# handler500 = 