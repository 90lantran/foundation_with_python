import movie
import fresh_tomatoes

bay_watch = movie.Movie("Bay Watch",
                  "team of safeguard in a California Beach",
                  "http://cdn1-www.comingsoon.net/assets/uploads/gallery/baywatch/screen-shot-2017-04-19-at-9-32-34-am-copy.jpg",
                  "https://www.youtube.com/watch?v=TDteZ0YrhSU")

game_of_thorones = movie.Movie("Game of Thrones",
                  "a fiction story to thrive for thrones",
                  "http://www.impawards.com/tv/posters/game_of_thrones_ver17_xlg.jpg",
                  "https://www.youtube.com/watch?v=giYeaKsXnsI")

vampire = movie.Movie("The Vampire Diaries",
                  "a fiction story about vampire in Mystic Falls",
                  "https://s-media-cache-ak0.pinimg.com/736x/26/22/0e/26220e4bc4b66f442310f26ebf7fcf3c.jpg",
                  "https://www.youtube.com/watch?v=w7Ab6zuZnV0")

movies = [bay_watch,game_of_thorones, vampire]

fresh_tomatoes.open_movies_page(movies)

