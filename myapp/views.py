from django.shortcuts import render
from django.http import HttpResponse
from  . models import Feature


def index(request):
    feature1 = Feature()    #feature1 inherits from Feature  model 
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'very fast  network experience'

    feature2 = Feature()    #feature2 inherits from picture model 
    feature2.id = 1
    feature2.name = 'Relable'
    feature2.details = 'very reliable network experience'

    feature3 = Feature()    #feature1 inherits from picture model 
    feature3.id = 2
    feature3.name = 'Easy'
    feature3.details = 'very easy to utilize or use experience'

    feature4 = Feature()    #feature1 inherits from picture model 
    feature4.id = 3
    feature4.name = 'Afordable'
    feature4.details = 'very affordable you dont have to braak the bank'

    feature5 = Feature()    #feature1 inherits from picture model 
    feature5.id = 4
    feature5.name = 'Execellence'
    feature5.details = 'be ready to experience excellence'

    

    features = [ feature1, feature2, feature3,feature4, feature5,]
    return render (request, 'index.html',{'features' : features,}) #pass this to the html 


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html',{'amount' : amount_of_words} )
