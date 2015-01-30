from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import InputRequired, Length, URL, Optional
from flask.ext.pagedown.fields import PageDownField


# frontend thread creation form
class ThreadForm(Form):

    subreddit = TextField('Subreddit', validators=[InputRequired()])

    title = TextField(
        'Title',
        validators=[
            InputRequired(),
            Length(
                max=300,
                message="Title cannot be longer than 300 characters"
            )
        ]
    )

    body = PageDownField(
        'Body',
        validators=[
            InputRequired(),
            Length(
                max=2500,
                message="Description cannot be longer than 2500 characters"
            )
        ]
    )

    link_facebook = TextField(
        'Facebook',
        validators=[
            Optional(),
            URL(require_tld=True)
        ]
    )
    link_twitter = TextField(
        'Twitter',
        validators=[
            Optional(),
            URL(require_tld=True)
        ]
    )
    link_youtube = TextField(
        'YouTube',
        validators=[
            Optional(),
            URL(require_tld=False)
        ]
    )
    link_soundcloud = TextField(
        'Soundcloud',
        validators=[
            Optional(),
            URL(require_tld=True)
        ]
    )
    link_bandcamp = TextField(
        'Bandcamp',
        validators=[
            Optional(),
            URL(require_tld=True)
        ]
    )
    link_website = TextField(
        'Official Website',
        validators=[
            Optional(),
            URL(require_tld=True)
        ]
    )
    link_label_website = TextField(
        'Label\'s Website',
        validators=[
            Optional(),
            URL(require_tld=True)
        ]
    )

    verification = TextField(
        'Verification Link',
        validators=[
            InputRequired(),
            URL(require_tld=True)
        ]
    )

    submit = SubmitField('Preview')


# delete thread form
class DeleteThreadForm(Form):
    submit = SubmitField('Confirm Delete')


# captcha form
class CaptchaForm(Form):
    captcha_response = TextField(
        '',
        validators=[
            InputRequired()
        ]
    )
    submit = SubmitField('Submit AMA')
