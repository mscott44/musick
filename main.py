
import webapp2
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ArtistsHandler(webapp2.RequestHandler):
    def get(self):
        artists_template = jinja_current_directory.get_template("templates/artists.html")
        self.response.write(artists_template.render())
class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        artist_template = jinja_current_directory.get_template("templates/artist.html")
        self.response.write(artist_template.render({"name": name}))
class SongsHandler(webapp2.RequestHandler):
    def get(self):
        songs_template = jinja_current_directory.get_template("templates/songs.html")
        self.response.write(songs_template.render())

class SongHandler(webapp2.RequestHandler):
    def get(self):
        song_template = jinja_current_directory.get_template("templates/song.html")
        self.response.write(song_template.render())


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template("templates/welcome.html")
        self.response.write(welcome_template.render())

class AlbumsHandler(webapp2.RequestHandler):
    def get(self):
        albums_template = jinja_current_directory.get_template("templates/albums.html")
        self.response.write(albums_template.render())
app = webapp2.WSGIApplication(
    [('/', WelcomeHandler),
    ('/artists', ArtistsHandler),
    ('/artist', ArtistHandler),
    ('/songs', SongsHandler),
    ('/albums', AlbumsHandler),
    ('/song', SongHandler),
    ], debug=True)
