from django.contrib import admin
from django.urls import path
from emissions.views import home, upload_csv, get_records

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('upload/', upload_csv),
    path('records/', get_records),
]
