from django.db import models
from django.core import validators
import re

# Create your models here.


def validator(self):
    if re.match(r"(\d{1,3}),(\d{1,3}),(\d{1,3})", self):
        return True
    else:
        raise validators.ValidationError(message="Please,enter correct rgb color. Example: '255,255,255' for white.")


class Home(models.Model):
    showing_blog_button = models.BooleanField(
        default=True, blank=True, null=True)
    button_color = models.CharField(
        validators=[validator], max_length=128, blank=True, null=True)
    e_mail = models.CharField(
        validators=[validators.EmailValidator(message="Please, enter corresponding email address")], max_length=128, blank=True, null=True)
    background_image_url1 = models.URLField(validators=[validators.URLValidator(
        message="Please, enter correct address")], max_length=250, blank=True, null=True)
    background_image_url2 = models.URLField(validators=[validators.URLValidator(
        message="Please, enter correct address")], max_length=250, blank=True, null=True)
    background_image_url3 = models.URLField(validators=[validators.URLValidator(
        message="Please, enter correct address")], max_length=250, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    About_link = models.URLField(
        validators=[validators.URLValidator], max_length=200, blank=True, null=True)
    Contact_link = models.URLField(
        validators=[validators.URLValidator], max_length=200, blank=True, null=True)
    title = models.CharField(max_length=50, null=True)
    Slogan = models.CharField(max_length=250, null=True)
    website_icon = models.ImageField(upload_to="ico/", blank=True, null=True)

    def Title(self):
        return self.title.upper()
