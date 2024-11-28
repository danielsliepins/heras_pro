from django.shortcuts import render

# Create your views here.
def sakums(request):
    return render(request, 'sakums.html')

def par_mums(request):
    return render(request, 'par_mums.html')

def pakalpojumi(request):
    return render(request, 'pakalpojumi.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def raksti_mums(request):
    return render(request, 'raksti_mums.html')

def atsauksmes(request):
    return render(request, 'atsauksmes.html')