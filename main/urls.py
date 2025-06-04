from django.urls import path

from main.views import HomeView, DownloadFileView


app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('national_cert/certificates/d203c1f3dd8ad15bdfa4b539aea9627e50de2.pdf', DownloadFileView.as_view(), name='download_file'),
]