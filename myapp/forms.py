from django import forms
from .models import Game,Prono,Team
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Div

class PronoForm(forms.Form):
    def __init__(self, user, *args, **kwargs):

		games = Game.objects.all()
		pronos = Prono.objects.filter(user=user)
		# self.helper = FormHelper()
		# helper.layout = Layout(
		# 	Div(
		# 		Div('score1_1',css_class="span6"),
		# 		Div('score2_1',css_class="span6"),
		# 	css_class="row-fluid"),
		# 	)

		super(PronoForm, self).__init__(*args, **kwargs)

		for i, item in enumerate(games):
			try:
				initial1 = pronos.get(game=item.id).score1
				initial2 = pronos.get(game=item.id).score2
			except:
				initial1 = 0
				initial2 = 0
			

			self.fields['score1_%s' % i] = forms.IntegerField(label=item.team1.short_name+" - "+item.team2.short_name,initial=initial1,min_value=0,max_value=15)
			self.fields['score2_%s' % i] = forms.IntegerField(label='',initial=initial2,min_value=0,max_value=15)
