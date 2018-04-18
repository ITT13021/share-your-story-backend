from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/user/', include('api.user.urls', namespace='user')),
    url(r'api/products/', include('api.products.urls', namespace='products')),
    url(r'api/news/', include('api.news.urls', namespace='news')),
]
