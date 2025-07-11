from django.urls import path

from main.views import HomeView, DownloadFileView, DownloadFile2View


app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('national_cert/certificates/d203c1f3dd8ad15bdfa4b539aea9627e50de2.pdf', DownloadFileView.as_view(), name='download_file'),
    path('cefr/certificates/43667e09b54fac8fefe205f96d5d5fda.pdf', DownloadFile2View.as_view(), name='download_file2'),
]