"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 处理静态文件
from rest_framework import routers
from wshop.settings import MEDIA_ROOT
from wshop.settings import STATIC_ROOT
from user import upload
from product.api import CategoryViewSet, GoodsViewSet

router = routers.DefaultRouter()
router.register(r'goods', viewset=GoodsViewSet)
router.register(r'category', viewset=CategoryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload.upload_image, name='upload_image'),
    url(r"^upload/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT}),

]
