from django.conf.urls import url, include
from rest_framework_bulk.routes import BulkRouter

from api.products.views import ProductsClassificationView, ProductsView, ProductsCollectView, ProductsMessageView

router = BulkRouter()

router.register(r'products', ProductsView, base_name='products')
router.register(r'productsclassification', ProductsClassificationView, base_name='productsclassification')
router.register(r'productscollect', ProductsCollectView, base_name='productscollect')
router.register(r'productsmessage', ProductsMessageView, base_name='productsmessage')

urlpatterns = router.urls

urlpatterns += [
]
