from django.http import HttpResponse, HttpResponseServerError
from .forms import FileUploadForm


def file_upload_view(request):
    form = FileUploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('')
    else:
        return HttpResponseServerError()
