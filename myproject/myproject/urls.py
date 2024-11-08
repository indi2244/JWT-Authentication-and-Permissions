from django.contrib import admin
from django.urls import path
from myapp.views import RegisterSerializer,RegisterView,LoginView,LogoutView, DashboardView,SpecialView,AdminOnlyView,ExampleView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/',RegisterView.as_view(), name="auth_register"),
    path('api/auth/login/',LoginView.as_view(), name="auth_login"),
    path('api/token/', TokenObtainPairView.as_view(), name='Token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/special/', SpecialView.as_view(), name='special-view'),
    path('api/adminonly/', AdminOnlyView.as_view(), name='adminonly-view'),
    path('example/', ExampleView.as_view(), name='example_view'),

]