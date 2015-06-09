# Import modules

                
import fresh_cherrytomatoes
import media
import os
import os.path
import sys
import urllib
import json
import re


# Store urls values
omdb = "http://www.omdbapi.com/?t="
youtube = "http://www.youtube.com/"
imdb = "http://www.imdb.com/"

# Movie Class
class Movie():

    
        # Create/Initiate an object instance of Movie
        def __init__(self,movie_title):
                self.title = movie_title


                # Function definition - Search youtube for movie_title passed from media.py, return trailer_youtube value
                def search_youtube():
                        search_text = self.title+" trailer official"
                        movie = {"search_query":search_text}
                        search = urllib.urlopen(youtube+'results'+"?"+urllib.urlencode(movie))
                        result = search.read()
                        search.close()       
                        match = re.search('\"yt-lockup-title\"\>\<a href=\"\/watch\?v\=([\w|\d|-|_]+)\"\s',result)
                        if match:
                                match.group(1)
                                trailer_youtube = youtube+'watch?v='+match.group(1)
                                return trailer_youtube


                # Function definition - Searches omdb for the movie_title passed from media.py, returns elements associated with thecontents of movie_title via api
                def search_omdb():           
                        connection = urllib.urlopen(omdb+self.title+"&y=&plot=short&r=json")
                        jsoninput = connection.read()
                        decoded = json.loads(jsoninput)
                        return decoded


                # Function definition - Uses the movie_title passed from media.py and the imdbID passed from search_omdb() to build the associated imdb url
                def search_imdb(decoded):
                        imdbURL = imdb +'title/'+decoded['imdbID']+"/?ref_=nv_sr_1"
                        # Plot, Poster, trailer_youtube,Released, Year, Genre,Director, Rated, Actors):           
                        return imdbURL


                # Function definition - Uses the dictionary passed from search_omdb api
                def omdb_detail(trailer_youtube,imdbURL,decoded):
                        self.storyline = decoded['Plot']
                        self.poster_image_url = decoded['Poster']
                        self.trailer_youtube_url = trailer_youtube
                        self.release_date = decoded['Released']
                        self.year = decoded['Year']
                        self.genre = decoded['Genre']
                        self.director = decoded['Director']
                        self.rating = decoded['Rated']
                        self.actors = decoded['Actors']
                        self.imdburl = imdbURL
                        return


                # Main function definition
                def main():
                        movie_trailer = search_youtube()
                        omdb_output = search_omdb()
                        imdb_output = search_imdb(omdb_output)
                        omdb_detail(movie_trailer,imdb_output,omdb_output)


                # Main function
                main()
                

