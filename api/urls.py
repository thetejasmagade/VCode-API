from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [

    re_path('^api/user/(?P<email>.+)/$', views.User.as_view()),
    path('api/users/', views.Users.as_view()),
    re_path('^api/code/(?P<email>.+)/(?P<codetitle>.+)/$',
            views.UserCode.as_view()),
    re_path('^api/codes/(?P<email>.+)/$', views.Codes.as_view()),
    
    # re_path('^api/user/(?P<email>.+)/$', views.UserDetails.as_view()),
    # path('api/codes/<str:pk>', views.UserCodes.as_view()),
    # path('api/users/<str:pk>/<str:codetitle>', views.UserCode.as_view()),
    # path('api/user/<str:pk>', views.UserData.as_view()),
    # re_path('^api/user/(?P<email>.+)/$', views.UserData.as_view()),
    # path('api/users/', views.Users.as_view()),
]
