from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator

def homepage(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')
    
#def eggs(request):
#    return HttpResponse('<h1>Eggs are great!</h1>')
def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()
    #counts = Counter(wordlist)
    #counts_word = counts.most_common(1)[0][0]
    #print('word: ' + counts_word)
    #
    #counts_qty = counts.most_common(1)[0][1]
    #print('qty: ' + str(counts_qty))
    #return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'word': counts_word, 'qty':counts_qty})
    worddict = {}
    
    for word in wordlist:
        if word in worddict:
            # Increase
            worddict[word] += 1
        else:
            #add to the dict
            worddict[word] = 1
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddict': sortedwords })