from django.shortcuts import render

# Create your views here.

def new_game(request):
	context = {'name': 'josh'}
	template = 'blackjack/home.html'
	return render(request, template, context)




def site_home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)
