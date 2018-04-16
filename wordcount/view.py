from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello sreekanth")
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordsall = fulltext.split()
    workdict = {}
    for word in wordsall:
        if word in workdict:
            workdict[word] += 1
        else:
            workdict[word] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordsall), 'wordcount': workdict.items})


def about(request):
    return render(request, 'about.html')
