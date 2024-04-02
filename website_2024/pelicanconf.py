from  markdown.extensions.toc import slugify_unicode

AUTHOR = 'PyCon Israel Team'
SITENAME = 'PyCon Israel 2024'
SITEURL = ""

SITESUBTITLE = (
    "PyCon Israel is a conference dedicated to the Python "
    "programming language, related technologies, and their use."
)

PATH = "content"

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'slugify': slugify_unicode,
        },
    },
    'output_format': 'html5',
}
# Blogroll
LINKS = (
    ("PyCon Israel 2023", "https://pycon.org.il/2023"),
    ("PyCon Israel 2022", "https://pycon.org.il/2022"),
    ("PyCon Israel 2021", "https://pycon.org.il/2021"),
    ("PyCon Israel 2019", "https://pycon.org.il/2019"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/pyconil/"),
    ("youtube", "https://www.youtube.com/@PyConIsrael"),
    ("facebook", "https://www.facebook.com/pyconisrael/"),
    ("linkedin", "https://www.linkedin.com/company/pycon-israel/"),
    ("mastodon", "https://tooot.im/@pyconil/"),
)

class PYCON:
    YEAR = 2024
    DATES = "16.9.2024"
    LOCATION = "Cinema City, Gelilot"

    SPONSORSHIP_AVAILABLE = True

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/PyCon-Israel-Flex"
STYLESHEET_URL = "/theme/css/pycon-israel-2024.css"

IMAGE_PROCESS = {}

PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

INDEX_SAVE_AS = 'blog_index.html'

def get_page_number(page):
    field = page.metadata.get('page_number', None)
    return int(field) if field else 0

PAGE_ORDER_BY = get_page_number
PAGE_SELECTION_FILTER = get_page_number

I18N_SUBSITES = {
    'he': {
        'SITENAME': 'פייקון ישראל 2024',
        'SITESUBTITLE': (
            'פייקון ישראל הוא כנס המוקדש לשפת התכנות פייתון, '
            'לטכנולוגיות הקשורות אליה, ולשימוש בהן'
        ),

    }
}

LANGUAGE_NAMES = {
    'en': "English",
    'he': "עברית",
}

COPYRIGHT_YEAR = 2024
COPYRIGHT_NAME = "Hamakor and individual contributors"
