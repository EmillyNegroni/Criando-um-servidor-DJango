from django.shortcuts import render

# Create your views here.
def Meu_app(request):
	return render(request, './index.html')