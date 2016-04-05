"""dj_lavang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from lavang.search_view import SearchMemberView
from lavang.family_member_view import NewFamilyView, EditFamilyView, EditMemberView, NewMemberView
from lavang import family_member_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^family/new/', NewFamilyView.as_view()),	
    url(r'^family/edit/(?P<id>\d+)/$', EditFamilyView.as_view()),		
    url(r'^member/new/(?P<famid>\d+)/$', NewMemberView.as_view()),	
    url(r'^member/edit/(?P<id>\d+)/$', EditMemberView.as_view()),		
    url(r'^search/$', SearchMemberView.as_view()),		
    url(r'', SearchMemberView.as_view()),			
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
	document_root=settings.MEDIA_ROOT)

