import os

from django.shortcuts import redirect
from django.views import View
from django.http import FileResponse


class HomeView(View):

    def get(self, req):

        return redirect('https://app.uzbmb.uz/')


class DownloadFileView(View):
    def get(self, req):
        file_path = 'media/1.pdf'
        if os.path.exists(file_path):
            return FileResponse(
                open(file_path, 'rb'),
                as_attachment=True,
                filename='d203c1f3dd8ad15ba4b539aea9627e50de2.pdf'
            )
        else:
            return redirect('https://app.uzbmb.uz/')
        

class DownloadFile2View(View):
    def get(self, req):
        file_path = 'media/1.pdf'
        if os.path.exists(file_path):
            return FileResponse(
                open(file_path, 'rb'),
                as_attachment=True,
                filename='43667e09b54fac8fefe205f96d5d5fda.pdf'
            )
        else:
            return redirect('https://app.uzbmb.uz/')
