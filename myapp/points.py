from .models import Team,Game,Prono


def games_played():
	games = Game.objects.all()
	games_played = [game for game in games if game.score1!=None] #add score2
	return games_played

def compute_points(user):
	ls_games = games_played()
	pronos = Prono.objects.filter(user=user)
	points, regular_pts, bonus_pts = 0, 0 ,0 
	for game in ls_games:
		prono = pronos.filter(game=game).first()
		if (prono.score1 - prono.score2)*(game.score1 - game.score2)>0:
			regular_pts +=3
		elif (prono.score1 - prono.score2) ==0 & (game.score1 - game.score2) == 0:
			regular_pts +=3
		if prono.score1 == game.score1 & prono.score2 == game.score2:
			bonus_pts +=1
	points = regular_pts + bonus_pts
	return [regular_pts,bonus_pts]




