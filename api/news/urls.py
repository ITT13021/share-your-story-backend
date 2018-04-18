from rest_framework_bulk.routes import BulkRouter

from api.news.views import NewsView, UserNewsView

router = BulkRouter()

router.register(r'news', NewsView, base_name='news')
router.register(r'usernews', UserNewsView, base_name='usernews')

urlpatterns = router.urls

urlpatterns += [
]
