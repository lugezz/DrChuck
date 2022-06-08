from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from .settings import STATICFILES_DIRS

print ("Nuevo", STATICFILES_DIRS[0])

urlpatterns = [
    #Base
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    path('admin/', admin.site.urls),
    #Propios
    path('authz/', include('authz.urls')),
    path('autos/', include('autos.urls')),
    path('chat/', include('chat.urls')),
    path('crispy/', include('crispy.urls')),
    path('forums/', include('forums.urls')),
    path('pics/', include('pics.urls')),
    path('prog/', include('programilla.urls')),
    path('form/', include('form.urls')),
    path('gp/', include('getpost.urls')),
    path('gview/', include('gview.urls')),
    path('menu/', include('menu.urls')),
    path('myarts/', include('myarts.urls')),
    path('route/', include('route.urls', namespace='nsroute')),
    path('session/', include('session.urls')),
    path('tmpl/', include('tmpl.urls')),
    
    # Serve the favicon
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': STATICFILES_DIRS[0],
        }
    ),
]


