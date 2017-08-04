# The Reel
The Reel uses python to create a static web page populated with your favorite movies and their trailers.

## Usage
- Uses the [OMDB API](http://www.omdbapi.com/) to pull movie information and poster.
- Movies are added by using their [IMDB](http://www.imdb.com/) identifier.
- Movie trailers must have a [YouTube](http://www.youtube.com) url.

New Movie objects can be added in `entertainment_center.py` by creating a new Movie instance. The first argument is the [IMDB](http://www.imdb.com/) identifier and the second argument is the [YouTube](http://www.youtube.com) url of the trailer.
```python
alien = media.Movie("tt0078748", "https://www.youtube.com/watch?v=f9tlCjlhNtE")
```


