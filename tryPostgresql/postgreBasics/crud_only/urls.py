from django.urls import path
from . import views

urlpatterns = [
    path('list_all/', views.product_list, name='list_all'),
    path('upload/', views.upload, name='upload'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('3dview/', views.render_view, name="renderview")
]
