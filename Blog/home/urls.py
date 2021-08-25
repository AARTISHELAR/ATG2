from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('welcome/',views.welcome_view,name='welcome'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('logout/',views.user_logout,name='logout'),
    path('read/<int:id>/',views.read_more,name='read'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)