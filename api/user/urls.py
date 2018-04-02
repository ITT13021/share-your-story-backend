from django.conf.urls import url
from rest_framework_bulk.routes import BulkRouter

from api.user.views import ProvinceView
from . import views

router = BulkRouter()

router.register(r'province', ProvinceView, base_name='province')

urlpatterns = router.urls

urlpatterns += [
]
