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
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/raspberrycheesecake'),
          ('Contact Me', 'hannah.hazi@cantab.net'),
          ('LinkedIn', 'https://www.linkedin.com/in/hannah-wray-9b985a84')
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/home/sandmanuser/pelican-themes/blue-penguin"

# Adding these to sort out pages  (I hope)
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images']
PAGES = ['about']
