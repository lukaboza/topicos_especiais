from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from app.views import router as app_router

router = NinjaAPI(openapi_url=None)
router.add_router('/', app_router)

urlpatterns = [
    path('', router.urls),
    path('admin/', admin.site.urls),
]
