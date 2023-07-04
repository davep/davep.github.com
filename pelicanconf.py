"""Configuration for my blog."""

##############################################################################
# General blog information.
AUTHOR          = "Dave Pearson"
SITENAME        = "blog.davep.org"
TIMEZONE        = "Europe/London"
DEFAULT_LANG    = "en"
DISQUS_SITENAME = "blogdaveporg"

##############################################################################
# General generation configuration.
THEME                   = "bootstrap2-dark"
PATH                    = "content"
DEFAULT_PAGINATION      = 10
ARTICLE_URL             = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS         = ARTICLE_URL
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS            = ["attachments"]

##############################################################################
# Feed information.
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/davep"),
)

# Social widget
SOCIAL = (
    ("Mastodon", "https://fosstodon.org/@davep"),
)

### pelicanconf.py ends here
