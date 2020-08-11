
from django.urls import path 
from .views import geo_search, sec_search
urlpatterns = [
path('geo/search/<str:country_name>/<str:query>/',geo_search),
path('sectors/<str:mongo_sector_id>/',sec_search)
]