from twitter_app.viewsets import TweetViewSet,UserViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('tweets',TweetViewSet)
router.register('Users',UserViewSet)