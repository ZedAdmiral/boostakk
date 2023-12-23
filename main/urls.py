from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import login_view
from boostakk import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('comment', views.comment, name='comment'),
    path('reviews', views.reviews, name='reviews'),
    path('login', login_view, name='login'),
    path('pro', views.pro, name='pro'),
    path('news', views.news, name='news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
