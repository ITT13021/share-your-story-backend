from rest_framework_bulk.routes import BulkRouter

from api.news.views import NewsView, NewsClassificationView

router = BulkRouter()

router.register(r'news', NewsView, base_name='news')
router.register(r'newsclassification', NewsClassificationView, base_name='newsclassification')

urlpatterns = router.urls

urlpatterns += [
]
