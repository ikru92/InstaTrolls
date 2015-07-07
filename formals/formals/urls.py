from django.conf.urls import patterns, include, url
from django.contrib import admin
from suggest import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from suggest import serializers

router = DefaultRouter()
router.register(r'post', views.PostsViewSet)
router.register(r'comment',views.CommentsViewSet)
router.register(r'love',views.LoveViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/?$', views.Auth.as_view()),
    url(r'^logout/', views.SignOut.as_view()),
    url(r'^feeds/$', views.FeedsViewSet.as_view({'get':'list'})),
    url(r'^commentlist/(?P<post_id>[0-9]+)/$', views.CommentList.as_view({'get':'list'})),
    url(r'^',include(router.urls)),
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
