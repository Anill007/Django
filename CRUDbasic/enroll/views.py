from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
# will add new and show items.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            # do not include to not save i.e leave blank
            reg = User(name=nm, email=em, password=pw)
            reg.save()

    fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add_show.html', {'form': fm, 'stu': stud})

# deletes at specific id
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')

#update items i.e edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/modify.html', {'form':fm})