from django.contrib import admin

# Register your models here.

from .models import Competition,Phase,Team,Game,Prono

class TeamModelAdmin(admin.ModelAdmin):
	list_display = ["name","group","short_name"]
	list_filter = ["group"]
	search_fields = ["name"]
	class Meta:
		model = Team

class GameModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","score1","score2","date_start","phase"]
	list_filter = ["phase"]
	list_editable = ["score1","score2"]
	search_fields = ["__unicode__"]
	class Meta:
		model = Team

class PronoModelAdmin(admin.ModelAdmin):
	list_display = ["user","game","score1","score2"]
	list_filter = ["user","game"]
	class Meta:
		model = Team

admin.site.register(Competition) 
admin.site.register(Phase) 
admin.site.register(Team, TeamModelAdmin) 
admin.site.register(Game, GameModelAdmin) 
admin.site.register(Prono, PronoModelAdmin) 