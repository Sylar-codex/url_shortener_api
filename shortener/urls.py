from rest_framework import routers
from .api import ShortenerViewset

router = routers.DefaultRouter()
router.register('api/shortener', ShortenerViewset)


urlpatterns = router.urls