# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField(u"Your book review",
                            validators=[DataRequired(message=u"the content can not be blank"), Length(1, 1024, message=u"Length should be under 1024")])
    submit = SubmitField(u"Add")
