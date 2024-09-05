from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from .api_service import get_random_recipe, get_recipe_details, search_recipes_by_ingredients
from rest_framework import viewsets
from .models import Recipe, Favorite
from .serializers import RecipeSerializer, FavoriteSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        # Logout the user and clear session
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_by_ingredients(request):
    """
    API endpoint to search for recipes by multiple ingredients.
    
    :param request: HTTP request containing the 'ingredients' query parameter
    :return: JSON response with the search results
    """
    ingredients = request.GET.get('ingredients', '')
    if not ingredients:
        return Response({'error': 'No ingredients parameter provided'}, status=400)

    number = int(request.GET.get('number', 10))  # Default to 10 if not provided
    data = search_recipes_by_ingredients(ingredients, number)
    return Response(data)



@api_view(['GET'])
@permission_classes([AllowAny])

def meal_detail(request, meal_id):
    """
    Fetch detailed information about a specific recipe by its ID.
    
    :param request: HTTP request containing the 'recipe_id' URL parameter
    :param recipe_id: The ID of the recipe
    :return: JSON response with the recipe details
    """
    data = get_recipe_details(meal_id)
    return Response(data)

@api_view(['GET'])
def random_meal(request):
    """
    Fetch a random recipe.
    
    :param request: HTTP request
    :return: JSON response with a random recipe
    """
    data = get_random_recipe()
    return Response(data)