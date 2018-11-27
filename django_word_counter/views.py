from django.http import HttpResponse
from django.shortcuts import  render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dict=dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1

    return render(request, 'count.html', dict(
        fulltext= fulltext,
        count=len(word_list),
        word_dict= sorted(word_dict.items(),  key=operator.itemgetter(1), reverse=True)
    ))

def about(request):
    return render(request, 'about.html')