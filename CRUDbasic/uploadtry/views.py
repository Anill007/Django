from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        # print(url)
        context['url'] = url
    return render(request, 'uploadtry/uploadfile.html', context)
