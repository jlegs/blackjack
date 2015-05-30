from django.db import models

# Create your models here.



class Deck(models.Model):
	number = models.IntegerField(unique=True, help_text='The deck number for this deck -- a way of grouping decks together')


class Card(models.Model):
	suit = models.ForeignKey('Suit', related_name='cards')
	deck = models.ForeignKey('Deck', related_name='cards')


class Suit(models.Model):
	name = models.CharField(max_length=15)










