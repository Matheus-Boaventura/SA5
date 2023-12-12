from django.urls import path
from app_aula5.views import home, update_dado, remove_dado

urlpatterns = [
    path('', home, name='home'),
    path('update/<int:dado_id>/', update_dado, name='update_dado'),
    path('remove/<int:dado_id>/', remove_dado, name='remove_dado'),
]