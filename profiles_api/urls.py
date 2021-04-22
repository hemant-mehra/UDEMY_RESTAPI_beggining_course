from django.urls import path,include
from profiles_api.views import HelloApiView,HelloVeiwSet
from rest_framework.routers import DefaultRouter

# used for viewsets
router=DefaultRouter()
router.register("hello-viewset",HelloVeiwSet,base_name="hello_viewset")


urlpatterns = [
    path('hello-view/',HelloApiView.as_view()),
    path("",include(router.urls))
]
