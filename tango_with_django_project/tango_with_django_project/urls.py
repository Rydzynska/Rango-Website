from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static

from django.contrib import admin
from rango import views

# from registration.backends.simple.views import RegistrationView

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self, user):
#         return url('register_profile')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', 
        views.MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/', 
        include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
