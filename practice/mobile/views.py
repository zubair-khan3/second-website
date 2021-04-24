from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.GET.get('text', 'default')
    print(text, "this is main text")
    final = text
    print(final, "this is final ")
    punc1 = ''' !@#$%^&*()_+{}[]|\:;"'<,>`.?/~'''
    result = ""
    for words in final:
        print(words, "this is word variable")
        if words not in punc1:
            result = result + words
            print(result, "this is result")
    return render(request, 'result.html', {'result': result, 'usertext': text})
