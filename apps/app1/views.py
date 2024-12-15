from django.shortcuts import render
from .models import Game 

# Create your views here.

def index(request):
    return render(request, "app1/index.html")

def listgames(request):
    game = Game.objects.all()
    return render(request, "app1/gameslist.html", {'games': game})


# def book(request,id):
#     book=get_object_or_404(Book, pk=id)
#     return render(request,"app1/book.html",{"book":book})