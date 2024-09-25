from .api import MovieAPI
from .gui import MovieRecommenderGUI
import tkinter as tk

class MovieApp:
    def __init__(self,api_key):
        self.api_key = api_key
        self.movie_api = MovieAPI(api_key)


    def run(self):
        root = tk.Tk()
        gui = MovieRecommenderGUI(root,self.movie_api)
        root.mainloop()
