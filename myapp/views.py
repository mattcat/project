from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Team,Game,Prono
from .forms import PronoForm
from points import compute_points


# Create your views here.

def teams(request):
	queryset = Team.objects.all()
	context = {
		"title" : "Teams",
		"teams_list" : queryset
	}
	return render(request, "teams.html", context)

def team_detail(request, id=None):
	instance = get_object_or_404(Team, id=id)
	games = (Game.objects.filter(team1=instance) | Game.objects.filter(team2=instance)).order_by("date_start")
	print type(games)
	print games
	context = {
		"instance" : instance,
		"games":games,
	}
	return render(request, "team_detail.html", context)

def games(request):
	queryset = Game.objects.all()
	context = {
		"title" : "Games",
		"games_list" : queryset
	}
	return render(request, "games.html", context)

def game_detail(request, id=None):
	instance = get_object_or_404(Game, id=id)
	pronos = Prono.objects.filter(game=instance)
	context = {
		"title" : instance,
		"instance" : instance,
		"pronos" : pronos,
	}
	return render(request, "game_detail.html", context)

def users(request):
	# if not request.user.is_staff:
	# 	raise Http404
	queryset = User.objects.all().order_by('username')
	table = [(el,compute_points(el)) for el in queryset]
	context = {
		"title" : "Home",
		"users_list" : queryset,
		"table" : table,
	}
	return render(request, "users.html", context)

def user_detail(request, id=None):
	instance = get_object_or_404(User, id=id)
	pronos = Prono.objects.filter(user=instance)
	context = {
		"title" : instance.username+"'s pronos",
		"instance" : instance,
		"pronos" : pronos,
	}
	return render(request, "user_detail.html", context)

@login_required(login_url='/login/')
def prono_create(request):
	user = request.user
	form = PronoForm(user, request.POST or None)
	if form.is_valid():
		games = Game.objects.all()
		
		for i,item in enumerate(games):
			score1 = form.cleaned_data.get("score1_"+str(i))
			score2 = form.cleaned_data.get("score2_"+str(i))

			try:
				obj = Prono.objects.get(user=user,game=games.get(id=item.id))
				obj.score1=score1
				obj.score2=score2
				obj.save()
			except:
				Prono.objects.create(user=user,game=games.get(id=item.id),score1=score1,score2=score2)


	context = {
		"form" : form,
	}
	return render(request, "prono_form.html",context)



