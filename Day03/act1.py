import os
import shutil

if not os.path.exists("movies"):
    os.mkdir("movies")
    print("'movies' folder created.")

source_file = "temp_movies.txt"
destination_file = "movies/"
print(destination_file)
if os.path.exists(source_file):
    shutil.move(source_file, destination_file)
    print("Moved and renamed temp_movies.txt to movies/movies_list.txt")
else:
    print("temp_movies.txt not found.")