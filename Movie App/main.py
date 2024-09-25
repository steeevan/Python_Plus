from app.lilapp import MovieApp


if __name__ == "__main__":
    API_KEY = "edbd150519b9111617f3da919556dc1f"
    app = MovieApp(API_KEY)
    app.run()