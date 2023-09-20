from django.urls import path
from.views import *

urlpatterns = [

    path('event',EventMainView.as_view(),name="evt"),
    path('select',EventSelect.as_view(),name="selectevt"),
    path('details/<int:id>',EventDetails.as_view(),name="evdt"),
    path('book/<int:id>',EventBook.as_view(),name="book"),
    path('bk',MyBooking.as_view(),name="bk"),
    path('del/<int:id>',cancelbooking,name="del")

    





    
]