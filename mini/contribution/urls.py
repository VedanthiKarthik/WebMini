from django.urls import path
from .import views

urlpatterns =[
    path('contribution',views.contribution,name='contribution'),
    path('showall',views.showall,name='showall'),
    path('about',views.about,name='about'),
    # path('add',views.add,name='add')
]