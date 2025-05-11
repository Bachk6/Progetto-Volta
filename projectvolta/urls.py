"""
URL configuration for projectvolta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from sitomuseo import views
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path("placeholder/",views.placeholder, name="placeholder"),
    path("home/",views.home, name="home"),
    path("detail/<int:opera_id>",views.detail,name="detail"),
    path("achievements/",views.achievement,name="achievements"),
    path("detail_achiv/<int:achievement_id>",views.detail_achiv,name="achievement"),
    path("user/",views.user,name="user"),
    path("",views.index,name="index"),
    path('autori/', views.lista_autori, name='lista_autori'),
    path('autore/<int:id>/', views.dettaglio_autore, name='dettaglio_autore'),
    path('registered/', lambda request: HttpResponse('Sei registrato!'), name='registered'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 