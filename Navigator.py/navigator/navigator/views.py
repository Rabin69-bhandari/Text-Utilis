# i am view created by rabin
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
 

def analyze(request):
    djtext= request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    upper = request.POST.get('Upper','off')
    lineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    

    if removepunc == 'on':
      punctions='''.,?!;:'"`()[]]}–—/"\''''
      analyze=""
      for char in djtext:
         if char not in punctions:
            analyze = analyze + char
      paramas={'Purpose':'Removed Punctuation','analyzedtext':analyze}
      djtext = analyze

         
    if upper == 'on':
             analyze=""
             analyze =djtext.upper()
             paramas={'Purpose':'Changed to Upper Case ','analyzedtext':analyze}
             djtext = analyze
    
    if lineremover == 'on':
      analyze=""
      for char in djtext:
         if char != "\n" and char != "\r":
            analyze = analyze + char
      paramas={'Purpose':'linew removing','analyzedtext':analyze}
      djtext = analyze
    
    if spaceremover == 'on':
      analyze=""
      for char in djtext:
         if char != " " and char !="  ":
            analyze = analyze + char
      paramas={'Purpose':'Space remover','analyzedtext':analyze}
      djtext = analyze
    
    if charcount == 'on':
       count = 0
       for char in djtext:
          if char != " ":
             count += 1
       analyze = count
       paramas={'Purpose':'Charcter count','analyzedtext':analyze}
       djtext = analyze
    return render(request,"analyze.html",paramas)

    
    

