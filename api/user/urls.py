from django.conf.urls import url
from rest_framework_bulk.routes import BulkRouter

from api.user.views import *

router = BulkRouter()

router.register(r'province', ProvinceView, base_name='province')
router.register(r'city', CityView, base_name='city')
router.register(r'School', SchoolView, base_name='School')
router.register(r'User', UserView, base_name='User')

urlpatterns = router.urls

urlpatterns += [
]
