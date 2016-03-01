from django.conf.urls import include, url
from django.contrib import admin
from blog.views import func1, func2, func3
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^shop1/$', func1, name='shop1'),
    url(r'^shop2/$', func2, name='shop2'),
    url(r'^shop3/$', func3),
]
