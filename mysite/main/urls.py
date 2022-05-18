from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path("", index.as_view(), name='index'),
    path("login", login.as_view(), name='login'),
    path("reg", reg.as_view(), name='reg'),
    path("logout", logout.as_view(), name='logout'),
    path("profile", profile.as_view(), name='profile'),
    path("addbook", addbook.as_view(), name='addbook'),
    path("addcategories", addcategories.as_view(), name='addcategories'),
    path("viewBook", viewBook.as_view(), name='viewBook'),
    path("viewCategories", viewCategories.as_view(), name='viewCategories'),
    path("info", info.as_view(), name='info'),
    path("addBookMe", addBookMe.as_view(), name='addBookMe'),
    path("deleteBookMe", deleteBookMe.as_view(), name='deleteBookMe'),
]
