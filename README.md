# The Reel
The Reel uses python to create a static web page populated with your favorite movies and their trailers. There are 12 pre-populated movies which can be removed or reordered. Users can add as many movies as they would like.

## Usage
- Uses the [OMDB API](http://www.omdbapi.com/) to pull movie information and poster.
- Movie information is queried using the [IMDB](http://www.imdb.com/) identifier.
- Movie trailers must have a [YouTube](http://www.youtube.com) url.

New Movie objects can be added in `entertainment_center.py` by creating a new Movie instance. The first argument is the [IMDB](http://www.imdb.com/) identifier and the second argument is the [YouTube](http://www.youtube.com) url of the trailer. The [IMDB](http://www.imdb.com/) identifier can be found in the url of the movie's [IMDB](http://www.imdb.com/) page. (e.g. imdb.com/title/**tt0078748**/?ref_=fn_al_tt_1)
```python
alien = media.Movie("tt0078748", "https://www.youtube.com/watch?v=f9tlCjlhNtE")
```

All new objects must also be added to the `movies` list.

```python
movies = [alien, big_fish, tremors]
```

Once all of the movies have been added, run the `entertainment_center.py` script to generate the web page.
