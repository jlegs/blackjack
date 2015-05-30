# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



def create_deck(apps, schema_editor):
    # We can't import the Deck, Card and Suit models directly as they may be a newer
    # version than this migration expects. We use the historical version.
    Deck = apps.get_model("blackjack", "Deck")
    Card = apps.get_model("blackjack", "Card")
    Suit = apps.get_model("blackjack", "Suit")

    


class Migration(migrations.Migration):

    dependencies = [
        ('blackjack', '0001_initial'),
    ]

    operations = [
    ]
