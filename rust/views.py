from django.shortcuts import render

def info(request):
    return render(request, 'rust/info.html')

def server_rules(request):
    return render(request, 'rust/server_rules.html')

def ingame_laws(request):
    return render(request, 'rust/ingame_laws.html')
