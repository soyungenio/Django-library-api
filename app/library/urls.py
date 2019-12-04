from django.urls import path

from .views import ListReadersView, CSVDataview

urlpatterns = [
    path('readers/<int:id>', ListReadersView.as_view(), name="readers-all"),
    path('data/csv', CSVDataview.as_view(), name="csv-data")
]
