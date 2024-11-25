import requests


api_url = "https://api.spoonacular.com/recipes/complexSearch"
api_key = "c0cef1272563483684104551eb97978e"  #replace api key pls
query_params = {
    # "query": "pasta",  
    "diet": "vegetarian",  
    "include_ingredients":"tomato,cheese",
    "ignorePantry": True,


    "apiKey": api_key
}

response = requests.get(api_url, params=query_params)


if response.status_code == 200:#good
    data = response.json()  
    print("Recipes found:", data)
else:#error
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response:", response.text)
