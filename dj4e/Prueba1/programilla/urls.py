from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'prog'

urlpatterns = [
    path('', views.helloworld) ,
    path('tracks/', views.tracks, name='tracks'),
    # Views de la clase
    # pre-defined class from Django
    path('tp', TemplateView.as_view(template_name='programilla/prueba.html')),
    # function from views.py
    path('funky', views.funky),
    path('danger', views.danger),
    path('danger2', views.danger2),
    path('game', views.game),
    path('rest/<int:guess>', views.rest),
    # Play with redirect
    path('bounce', views.bounce),
    # our class from views.py
    path('main', views.MainView.as_view()),
    path('remain/<slug:guess>', views.RestMainView.as_view()),
    path('remain2/<slug:guess>', views.RestMainView.as_view()),

    # Otros
    path('juego1/<int:num>', views.Juego1.as_view())
]