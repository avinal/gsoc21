#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = 'Avinal Kumar'
HIDE_AUTHORS = True
SITENAME = "New Buildsystem and CI/CD"
SITESUBTITLE = 'A GSoC project by Avinal Kumar'
SITEURL = 'https://gsoc.avinal.space'
THEME = 'themes/alchemy'
PATH = 'content'
MAIL = 'blog@avinal.space'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

ARTICLE_IMAGE = '/images/gsoc-fossology.gif'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL Flexibility
ARTICLE_URL = 'posts/{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# static content setting
STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/site.webmanifest': {'path': 'site.webmanifest'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/mstile-70x70.png': {'path': 'mstile-70x70.png'},
    'extras/mstile-310x310.png': {'path': 'mstile-310x310.png'},
    'extras/mstile-144x144.png': {'path': 'mstile-144x144.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    'extras/CNAME': {'path': 'CNAME'},
}

RFG_FAVICONS = True

LINKS = [
    ('about me', "https://avinal.space"),
    
]

# icons
ICONS = [
    ('google', 'https://summerofcode.withgoogle.com/projects/#4535841440923648'),
    ('github', "https://github.com/avinal/fossology/tree/avinal/feat/cmake-buildsystem"),
    ('linkedin', 'https://www.linkedin.com/in/avinal/')
]

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

DEFAULT_PAGINATION = 10

PYGMENTS_STYLE = 'manni'


# Comments config

FORM_COMMENTS = True

FORM_PROPERTIES = {
    'name' : 'entry.982725972',
    'email':'entry.1652853191',
    'link':'entry.1641222305',
    'comment':'entry.1062656232',
    'action':'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfL9T8WBRm-Ac2uyu74lJXSYOqAuF6lLIUAulRArCsuiI1ZRQ/formResponse'
}

DEFAULT_METADATA = {
    'status': 'draft',
}

