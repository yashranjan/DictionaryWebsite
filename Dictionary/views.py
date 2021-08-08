# 3rd Party imports
import requests,json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Word
from .forms import WordModelForm

# Create your views here.
def home_view(request):
    context = {
        'page_title':'Dictionary Page',
        'form':None,
        'ansList':{}
    }
    form = WordModelForm(request.GET or None)
    if form.is_valid():
        key = form.cleaned_data['value']
        key = key.lower()
        obj = Word.objects.filter(value=key)
        if not obj:
            # Fetch the data for the word | Store in DB
            apiStr = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'
            data = requests.get(url=apiStr+key)
            if data.status_code == 200:
                dataList = json.loads(data.content)
                print(dataList)
                for data in dataList:
                    if data['meanings'][0]['partOfSpeech']:
                        for meaning in data['meanings']:
                            dataDict = {
                                'value':key,
                                'partOfSpeech':meaning['partOfSpeech'],
                                'synonym':None,
                                'antonym':None,
                                'meaning':None
                            }

                            if meaning['definitions']:
                                dataDict['meaning'] = meaning['definitions'][0]['definition']
                                dataDict['antonym'] = meaning['definitions'][0]['antonyms'] and meaning['definitions'][0]['antonyms'][0]
                                dataDict['synonym'] = meaning['definitions'][0]['synonyms'] and meaning['definitions'][0]['synonyms'][0]
                            Word.objects.create(**dataDict)
            else:
                # Neither stored in DB nor found
                obj = []
        
        obj = Word.objects.filter(value=key)
        context['ansList']=obj
        context['key']=key
        form = WordModelForm()

    context['form']=form
    return render(request,"home.html",context)

def show_all_words_view(request):
    wordsList = Word.objects.all()
    context = {
        'page_title':'List words',
        'wordsList':wordsList
    }

    return render(request,"words.html",context)