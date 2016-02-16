from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_home(request):
	return HttpResponse("<h1>Hello</h1>")
def post_list(request):
	return render(request, "index.html", {})