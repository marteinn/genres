# Genres
Genres is a python library (2.7) that guesses the genres for text with musical context.

## How it works
Genres is based on a list of genres and tags (database), that are compared against supplied text using regexp, found genres are then compared agains its main category to avoid mismatches.

## Usage

The api is simple.

    import genres
    r = genres.find("Pink Floyd is a great rock band)
    r
    ["Rock]

You can also supply your own database.

    import genres

    db_obj = genres.db.Db("./example.txt")
    finder_obj = genres.finder.Finder(db_obj)


## Database

The database is a simple list of words, separated by newline and structured like this:

|Data|Description|
|-------------|:-------------:|
|Rock|Main category|
|Rock|Sub category|
|-Pink Floyd|Tag associated to category rock|
|#Test|Comment|
||Categories are sparated with newline|
|Jazz|...|
|Post-bop|...|

Genres are distributed with a database that can be found under `genres/data.txt` and the genre structure is based on [Allmusic genre categorisation](http://en.wikipedia.org/wiki/List_of_popular_music_genres).


## Installation
Genres can easily be installed through pip.

    $ pip install genres


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Android-AppLog is released under the [MIT License](http://www.opensource.org/licenses/MIT).
