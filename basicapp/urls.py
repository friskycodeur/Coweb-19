from django.urls import path
from basicapp import views

app_name='basicapp'

urlpatterns=[
  path('tracker/',views.tracker,name='tracker'),
  path('form_page/',views.form_name_view,name='form_page'),
  path('advisory/',views.advisory,name='advisory'),
  path('docbot/',views.docbot,name='docbot'),
]