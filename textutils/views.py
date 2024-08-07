#created by me 
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    #get text
    djtext = request.POST.get('text', 'default')
    #checkboxes state
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    # to remove punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    # to captialise
    if fullcaps=="on":
         analyzed=""
         for char in djtext:
             analyzed=analyzed+char.upper()
         params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
         djtext = analyzed
         #return render(request, 'analyze.html', params)
    if newlineremover=="on":
         analyzed=""
         for char in djtext:
             if char != "\n" and char!="\r":
                 analyzed = analyzed+char
         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
         djtext = analyzed
         #return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
             if not(djtext[index] == " " and djtext[index+1]==" "):
                 analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if charcount=="on":
         analyzed = ""
         Count = 0
         for char in djtext:
             Count +=1
         params = {'purpose': 'Characters in text', 'analyzed_text': Count}
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)
