import tkinter as tk
from tkinter import messagebox

class MovieRecommenderGUI:
    def __init__(self,master,movie_api):
        self.master = master
        self.movie_api = movie_api
        self.current_movie = None

        self.setup_gui()

    def setup_gui(self):
        self.master.title("Movie Recommendation System")
        
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)

        results_frame = tk.Frame(self.master)
        results_frame.pack(pady=10)

        actions_frame = tk.Frame(self.master)
        actions_frame.pack(pady=10)

        label = tk.Label(input_frame,text="Enter Movie title:")
        label.grid(row=0,column=0,padx=10)

        self.entry = tk.Entry(input_frame, width=50)
        self.entry.grid(row=0, column=1, padx=10)

        button = tk.Button(input_frame, text="Search", command=self.search_and_display)
        button.grid(row=0, column=2, padx=10)

        self.text_box = tk.Text(results_frame, height=20, width=75)
        self.text_box.pack()

        genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller"]
        self.genre_var = tk.StringVar(self.master)
        self.genre_var.set("Select Genre")

        genre_menu = tk.OptionMenu(actions_frame,self.genre_var,*genres)
        genre_menu.grid(row=0,column=0,padx=10)

        filter_button = tk.Button(actions_frame,text="Filter by Genre", command=self.filter_by_genre)
        filter_button.grid(row=0, column=1, padx=10)

        save_button = tk.Button(actions_frame,text="Save to Favorites", command=self.save_to_favorites)
        save_button.grid(row=0,column=2,padx=10)

        self.listbox = tk.Listbox(actions_frame,height=6,selectmode=tk.SINGLE)
        self.listbox.grid(row=1,columnspan=3,pady=10)

    def search_and_display(self):
        title = self.entry.get()
        if title:
            movies = self.movie_api.search_movie(title)
            if movies:
                if len(movies) > 1:
                    self.listbox.delete(0,tk.END)
                    for movie in movies:
                        self.listbox.insert(tk.END,movie['title'])
                        self.listbox.bind("<<ListboxSelect>>", lambda evt: self.movie_details(movies[self.listbox.curselection()[0]]))
                else:
                    self.show_movie_details(movies[0])
            else:
                messagebox.showerror("Error","movie not found")
        else:
            messagebox.showwarning("input required","Please enter a movie title")

    def movie_details(self,movie):
        movie_details = self.movie_api.get_movie_details(movie['id'])
        self.current_movie = movie_details
        if movie_details:
            details = self.display_movie_details(movie_details)
            recommendations = self.movie_api.get_recommendations(movie['id'])
            if recommendations:
                recs = self.display_recommendations(recommendations)
                details += f"\n\n{recs}"
            else:
                details += "\n\n No Recommendations found"
            self.text_box.delete("1.0",tk.END)
            self.text_box.insert(tk.END,details)
        else:
            messagebox.showerror("ERROR", "Movie details not found")
    

    def filter_by_genre(self):
        selected_genre = self.genre_var.get()
        movie_title = self.entry.get()
        if selected_genre and movie_title:
            self.search_and_display()
    
    def save_to_favorites(self):
        if self.current_movie:
            with open("favorites.txt", "a") as file:
                file.write(f"{self.current_movie['title']} - {self.current_movie['overview']} (Rating: {self.current_movie['vote_average']}/10)\n\n")
                messagebox.showinfo("Saved", f"{self.current_movie['title']} has been saved to favorites!")
    def display_movie_details(self,movie):
        details = f"{self.current_movie['title']} - {self.current_movie['overview']} (Rating: {self.current_movie['vote_average']}/10)\n\n"
        return details

    def display_recommendations(self,recommendations):
        recs = ""
        for idx, movie in enumerate(recommendations,1):
            movie_details = self.movie_api.get_movie_details(movie['id'])
            rating = movie_details['vote_average'] if movie_details else "N/A"
            recs += f"{idx}, {movie['title']} (Rating: {rating}/10)\n"
        return recs
    
            


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommenderGUI(root,"sadasdasgregerreg")

