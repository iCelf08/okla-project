from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'favorites', views.FavoriteViewSet)

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.UserDetailView.as_view(), name='user_detail'),
    path('logout/', views.LogoutView.as_view(), name='token_blacklist'),
    path('', include(router.urls)),
    path('search-by-ingredients/', views.search_by_ingredients, name='meal_search'),
    # path('recipe-details/', views.meal_detail, name='meal_information'),
    path('meal/<str:meal_id>/', views.meal_detail, name='meal_detail'),
    path('random/', views.random_meal, name='random_meal'),
]
