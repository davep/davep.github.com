"""Configuration for my blog."""

##############################################################################
# General blog information.
AUTHOR          = "Dave Pearson"
SITENAME        = "blog.davep.org"
TIMEZONE        = "Europe/London"
DEFAULT_LANG    = "en"
DISQUS_SITENAME = "blogdaveporg"
SITELOGO        = "static/davep.jpeg"

##############################################################################
# General generation configuration.
PATH                    = "content"
DEFAULT_PAGINATION      = 10
ARTICLE_URL             = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS         = ARTICLE_URL
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS            = ["attachments", "static"]
DATE_FORMATS            = {"en": "%Y-%m-%d"}

##############################################################################
# Theme control.
THEME                                      = "flex"
THEME_COLOR                                = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE           = True
CUSTOM_CSS                                 = "static/davep.css"

##############################################################################
# Feed information.
FEED_ALL_ATOM         = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM    = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

##############################################################################
# Menu configuration.
MAIN_MENU = True
LINKS = (
    ("GitHub", "https://github.com/davep"),
)
SOCIAL = (
    ("Mastodon", "https://fosstodon.org/@davep"),
)
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

### pelicanconf.py ends here
