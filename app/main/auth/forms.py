# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"I forgot to fill it out.!"), Length(1, 64), Email(message=u"Are you sure this is Email?")])
    password = PasswordField(u'password', validators=[DataRequired(message=u"I forgot to fill it out.!"), Length(6, 32)])
    remember_me = BooleanField(u"Keep my login status", default=True)
    submit = SubmitField(u'Sign in')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"I forgot to fill it out.!"), Length(1, 64), Email(message=u"Are you sure this is Email?")])
    name = StringField(u'username', validators=[DataRequired(message=u"I forgot to fill it out.!"), Length(1, 64)])
    password = PasswordField(u'password',
                             validators=[DataRequired(message=u"I forgot to fill it out.!"), EqualTo('password2', message=u'Passwords must match'),
                                         Length(6, 32)])
    password2 = PasswordField(u'Confirm password again', validators=[DataRequired(message=u"I forgot to fill it out.!")])
    submit = SubmitField(u'registered')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'This Email has already been registered')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'old password', validators=[DataRequired(message=u"I forgot to fill it out.!")])
    new_password = PasswordField(u'new password', validators=[DataRequired(message=u"I forgot to fill it out.!"),
                                                     EqualTo('confirm_password', message=u'Passwords must match'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Confirm the new password', validators=[DataRequired(message=u"I forgot to fill it out!")])
    submit = SubmitField(u"Save password")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'The original password is wrong')
