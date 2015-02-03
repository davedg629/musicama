from __future__ import division
from flask import flash
import re
from unicodedata import normalize
from os import urandom
from base64 import urlsafe_b64encode


# flash errors
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the {} field - {}".format(
                getattr(form, field).label.text,
                error
            ), 'error')


# generate a random token
def generate_token():
    return urlsafe_b64encode(urandom(30)).rstrip("=")


# turn text into slug
def make_slug(text, delim=u'-'):
    """Generates a slightly worse ASCII-only slug."""
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


# get time ago from datetime
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff // 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff // 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff // 30) + " months ago"
    return str(day_diff // 365) + " years ago"


# construct reddit post body
def reddit_body(desc,
                facebook,
                twitter,
                youtube,
                soundcloud,
                bandcamp,
                website,
                label_website,
                verify):
    body = desc
    if facebook or twitter \
            or youtube or soundcloud \
            or bandcamp or website \
            or label_website:
        body = body + '\n\n-\n\n**Links**\n\n-\n\n'
        if facebook:
            body = body + '* [Facebook](' + facebook + ')\n'
        if twitter:
            body = body + '* [Twitter](' + twitter + ')\n'
        if youtube:
            body = body + '* [YouTube](' + youtube + ')\n'
        if soundcloud:
            body = body + '* [Soundcloud](' + soundcloud + ')\n'
        if bandcamp:
            body = body + '* [Bandcamp](' + bandcamp + ')\n'
        if website:
            body = body + '* [Official Website](' + website + ')\n'
        if label_website:
            body = body + '* [Label\'s Website](' + label_website + ')\n'
    body = body + '\n\n-\n\n**Verification:** ' + verify
    return body
