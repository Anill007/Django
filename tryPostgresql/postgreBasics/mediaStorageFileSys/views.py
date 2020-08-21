from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os

# Create your views here.


def upload(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES['doc']
        #settings.MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media1')
        fs = FileSystemStorage()
        name = fs.save(file.name, file)
        url = fs.url(name)
        print(name + "  " + url)
        context['url'] = url
    return render(request, 'filesys/base.html', context)
