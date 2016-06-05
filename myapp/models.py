from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     striker = models.CharField(max_length=30,default="Neymar")


# Create your models here.

class Competition(models.Model):
	name = models.CharField(max_length=30)
	date_start = models.DateTimeField()
	date_end = models.DateTimeField()

	def __unicode__(self):
		return self.name

class Phase(models.Model):
	name = models.CharField(max_length=30)
	date_start = models.DateTimeField()  #to be deleted
	date_end = models.DateTimeField()    #to be deleted

	def __unicode__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=20)
	group = models.CharField(max_length=1)
	short_name = models.CharField(max_length=3, default = "FRA")

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("team_detail", kwargs={"id":self.id})

class Game(models.Model):
	team1 = models.ForeignKey(Team, null=True, related_name='team1')
	team2 = models.ForeignKey(Team, null=True, related_name='team2')
	score1 = models.IntegerField(null=True, blank=True)
	score2 = models.IntegerField(null=True, blank=True)
	date_start = models.DateTimeField()
	phase = models.ForeignKey(Phase, null=True)
	competition = models.ForeignKey(Competition, null=True)

	def __unicode__(self):
		return self.team1.name+" - "+self.team2.name

	def get_absolute_url(self):
		return reverse("game_detail", kwargs={"id":self.id})
	# @property
	def is_played(self):
		return self.score1 != None

class Prono(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	game = models.ForeignKey(Game)
	score1 = models.IntegerField(blank=False)
	score2 = models.IntegerField(blank=False)

	class Meta:
		unique_together = ('user','game')
