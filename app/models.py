from django.db import models
from django.utils.timezone import datetime
import random, string



def random_string():
    return ''.join(random.choices(string.ascii_letters.lower() + string.digits, k=5))


class Link(models.Model):

    id = models.CharField(
        primary_key = True,
        max_length = 5,
        default = random_string, 
        editable = True, 
        unique = True, 
        blank = False, 
        null = False
        )
    
    title = models.CharField(
        max_length = 100, 
        default = '',
        verbose_name = 'Name or Title',
        help_text = 'Enter the preferred name for the link you want to save',
        blank = False, 
        null = False
        )
    
    url = models.URLField(
        max_length = 200,
        unique = True,
        verbose_name = 'URL',
        help_text = 'Enter the URL',
        blank = False,
        null = False
    )

    time_saved = models.DateTimeField(
        default = datetime.now,
        editable = True,
        blank = False, 
        null = False
        )

        

    def __str__(self):
        return self.title
