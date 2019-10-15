#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hannah Hazi'
SITENAME = u'Hannah Clare Wray Hazi'
SITESUBTITLE = 'I love making beautiful things.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget SOCIAL
SOCIAL = (('GitHub', 'https://github.com/raspberrycheesecake'),
          ('Contact Me', 'mailto:hannah.hazi@cantab.net'),
          ('LinkedIn', 'https://uk.linkedin.com/in/hannah-hazi-9b985a84')
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/home/hannah/Documents/Python/Website/themes/blue-penguin"

# Adding these to sort out pages  - hm, still not working.
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images']

MENUITEMS = SOCIAL
DISPLAY_MENU = True

ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'

ABOUT_URL = 'about'
ABOUT_SAVE_AS = 'about/index.html'
# Tried adding ('About', ABOUT_URL, ABOUT_SAVE_AS) to MENU_INTERNAL_PAGES, didn't work. Damn...

MENU_INTERNAL_PAGES = (('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),)

