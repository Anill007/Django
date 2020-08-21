"""CRUDbasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from enroll import views as v1
from uploadtry import views as v2
from uploadImageModelForm import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.add_show, name='addandshow'),
    path('delete/<int:id>/', v1.delete_data, name='deletedata'),
    path('update/<int:id>/', v1.update_data, name='updatedata'),

    path('upload/', v2.upload, name='upload'),

    # uploadImageModelForm
    path('v3/upload/', v3.prod_upload, name='produpload'),
    path('v3/list/', v3.prod_list, name='prodlist'),
    path('v3/delete/<int:id>', v3.prod_del, name='proddel'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
