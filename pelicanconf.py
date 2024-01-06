"""Configuration for my blog."""

##############################################################################
# General blog information.
AUTHOR           = "Dave Pearson"
SITENAME         = "blog.davep.org"
SITETITLE        = "davep"
SITESUBTITLE     = "Code, Emacs, VR, Stuff..."
TIMEZONE         = "Europe/London"
DEFAULT_LANG     = "en"
#DISQUS_SITENAME  = "blogdaveporg"
SITELOGO         = "/static/davep.jpeg"
FAVICON          = "/static/favicon.ico"
COPYRIGHT_NAME   = AUTHOR
COPYRIGHT_YEAR   = "2015-2024"

##############################################################################
# General generation configuration.
PATH                    = "content"
DEFAULT_PAGINATION      = 10
ARTICLE_URL             = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS         = ARTICLE_URL
YEAR_ARCHIVE_SAVE_AS    = "{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS   = "{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS     = "{date:%Y}/{date:%m}/{date:%d}/index.html"
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS            = ["attachments", "static", "extras"]
DEFAULT_DATE_FORMAT     = "%Y-%m-%d %H:%M %z"
FILENAME_METADATA       = r"\d{4}-\d{2}-\d{2}-(?P<slug>.*)"
EXTRA_PATH_METADATA     = {"extras/CNAME": {"path": "CNAME"}, "static/humans.txt": {"path": "humans.txt"}}
SUMMARY_MAX_LENGTH      = 1_000_000
ROBOTS                  = "all"

##############################################################################
# Plugin control.
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS      = ["neighbors", "post_stats"]

##############################################################################
# Theme control.
THEME                                      = "flex"
THEME_COLOR                                = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE           = True
CUSTOM_CSS                                 = "static/davep.css"

##############################################################################
# Feed information.
FEED_MAX_ITEMS        = 20
FEED_ALL_ATOM         = "feeds/all.atom.xml"
FEED_ALL_RSS          = "feed.xml"
CATEGORY_FEED_ATOM    = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

##############################################################################
# Menu configuration.
MAIN_MENU        = True
LINKS_IN_NEW_TAB = "all"
LINKS            = (
    ("davep@", "http://davep.at/"),
    ("Pinboard", "https://pinboard.in/u:davep"),
    ("Photoblog", "https://seenbydavep.blogspot.com/"),
    ("Emacs Packages", "https://elisp.dev/"),
    ("Python Packages", "https://pypi.org/user/davepearson/"),
)
SOCIAL           = (
    ("github", "https://github.com/davep"),
    ("mastodon", "https://fosstodon.org/@davep"),
    ("flickr", "https://www.flickr.com/photos/davepearson/"),
    ("lastfm", "https://www.last.fm/user/davepdotorg"),
    ("npm", "https://www.npmjs.com/~davep.org"),
    ("youtube", "https://www.youtube.com/user/daveporg"),
    ("steam", "https://steamcommunity.com/id/davepdotorg")
)
MENUITEMS        = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

### pelicanconf.py ends here
