from django.conf.urls import url, include
from rest_framework_bulk.routes import BulkRouter

from api.user.views import ProvinceView, CityView, SchoolView, UserView, login

router = BulkRouter()

router.register(r'province', ProvinceView, base_name='province')
router.register(r'city', CityView, base_name='city')
router.register(r'school', SchoolView, base_name='School')
router.register(r'user', UserView, base_name='User')

urlpatterns = router.urls

urlpatterns += [
    url(r'^login$', login, name='login'),
]
