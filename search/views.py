from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    return render(request, 'index.htm')

def word(request):

    word = request.GET['word']

    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://www.thesaurus.com/browse/'+word)
    

    if res:
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

        synonyms = soup2.find_all('a', {'class': 'css-r5sw71-ItemAnchor etbu2a31'})
        ss = []
        for b in synonyms[0:]:
            re = b.text.strip()
            ss.append(re)
        se = ss
        

        

        antonyms = soup2.find_all('a', {'class': 'css-lqr09m-ItemAnchor etbu2a31'})
        aa = []
        for c in antonyms[0:]:
            r = c.text.strip()
            aa.append(r)
        ae = aa
    else:
        se = ''
        ae = ''


    results = {
        'word' : word,
        'meaning' : meaning1,
    }


    return render(request, 'word.htm', {'se': se, 'ae': ae, 'results': results})