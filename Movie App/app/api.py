import requests
class MovieAPI:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self,api_key):
        self.api_key = api_key

    def search_movie(self, title):
        search_url = f"{self.BASE_URL}/search/movie"
        params = {
            'api_key': self.api_key,
            'query': title
        }
        response = requests.get(search_url, params=params)

        if response.status_code == 200:
            return response.json()['results']
        else:
            return None
        
    def get_recommendations(self,movie_id, genre_filter=None):
        recommendations_url = f"{self.BASE_URL}/movie/{movie_id}/recommendations"
        params = {
            'api_key': self.api_key
        }

        response = requests.get(recommendations_url,params=params)
        if response.status_code == 200:
            recommendation = response.json()['results']
            if genre_filter:
                recommendation = [movie for movie in recommendation if genre_filter in [genre['name'] for genre in movie['genre)ids']]]
            return recommendation
        else:
            return None
    