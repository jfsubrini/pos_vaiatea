"""pos_vaiatea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from stocks.admin import admin_bar_stock, admin_kitchen_stock, admin_goodies_stock


admin.site.site_header = 'Vaiatea Administration'
# admin.site.site_title = 'Vaiatea Site Admin'
admin.site.index_title = 'Vaiatea Liveaboard Indonesia'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('billing/', include('billing.urls')),
    path('schedule/', include('schedule.urls')),
    path('stocks/', include('stocks.urls')),
    # path("stock/bar/", admin_bar_stock.urls),
    # path("stock/kitchen/", admin_kitchen_stock.urls),
    # path("stock/goodies/", admin_goodies_stock.urls),
]
