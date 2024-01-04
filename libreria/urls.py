from django.urls import path, include
from rest_framework import routers
from libreria import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)

# Rutas necesarias: 
# POST /auth/register
# POST /auth/login
# GET /books
# POST /books
# DELETE /books/:id

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/login/', views.TokenObtainView.as_view(), name='token_obtain_view'),
    path('auth/register/', views.UserRegisterView.as_view(), name='user_register_view'),
]
