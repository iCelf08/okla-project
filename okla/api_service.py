import requests

# Replace 'YOUR_SPOONACULAR_API_KEY' with your actual Spoonacular API key
SPOONACULAR_API_KEY = 'd6ea58ce0dff453ea2dee8443e88e500'
SPOONACULAR_API_URL = 'https://api.spoonacular.com/recipes'

def search_recipes_by_ingredients(ingredients, number=12):
    """
    Search for recipes by multiple ingredients.
    
    :param ingredients: A comma-separated list of ingredients (e.g., 'chicken,onion')
    :param number: Number of recipes to return
    :return: JSON response from the API containing recipe search results
    """
    url = f"{SPOONACULAR_API_URL}/findByIngredients"
    params = {
        'ingredients': ingredients,
        'number': number,
        'apiKey': SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

def search_recipes(query, number=18):
    """
    Search for recipes by a search query.
    
    :param query: The search query string (e.g., 'chicken soup')
    :param number: Number of recipes to return
    :return: JSON response from the API containing recipe search results
    """
    url = f"{SPOONACULAR_API_URL}/complexSearch"
    params = {
        'query': query,
        'number': number,
        'apiKey': SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

def get_recipe_details(recipe_id):
    """
    Get details of a specific recipe by its ID.
    
    :param recipe_id: The ID of the recipe (e.g., '654959')
    :return: JSON response from the API containing recipe details
    """
    url = f"{SPOONACULAR_API_URL}/{recipe_id}/information"
    params = {'apiKey': SPOONACULAR_API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def get_random_recipe():
    """
    Get a random recipe.
    
    :return: JSON response from the API containing a random recipe
    """
    url = f"{SPOONACULAR_API_URL}/random"
    params = {'apiKey': SPOONACULAR_API_KEY}
    response = requests.get(url, params=params)
    return response.json()

# Example usage:
if __name__ == "__main__":
    ingredients = "chicken,onion"
    recipes = search_recipes_by_ingredients(ingredients)
    print("Recipes with ingredients:", recipes)

    query = "chicken soup"
    search_results = search_recipes(query)
    print("Search results:", search_results)

    if search_results.get('results'):
        recipe_id = search_results['results'][0]['id']
        recipe_details = get_recipe_details(recipe_id)
        print("Recipe details:", recipe_details)

    random_recipe = get_random_recipe()
    print("Random recipe:", random_recipe)
