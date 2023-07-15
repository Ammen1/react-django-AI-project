from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView,UserDetail

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('userdetail/', UserDetail.as_view(), name='userdetail') ,    
]
