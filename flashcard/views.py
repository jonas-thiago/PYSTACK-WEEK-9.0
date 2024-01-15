from django.shortcuts import render

# Create your views here.

def novo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'novo_flashcard.html',
        )