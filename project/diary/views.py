from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Person

# Create your views here.
def display(request, year=2020):
    people = Person.objects.all()
    years_wise = {}
    for p in people:
        if p.year not in years_wise.keys():
            years_wise[p.year] = []
        years_wise[p.year].append(p)

    if year in years_wise.keys():
        template = loader.get_template('diary/index.html')
        keys = []
        for i in years_wise.keys():
            keys.append(i)
        keys.sort(reverse=True)
        context = {
            'people':years_wise[year],
            'years':keys,
            'cur_year':year
        }
        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('diary/index.html')
        context = {
            'years':years_wise.keys()
        }
        return HttpResponse(template.render(context, request))

def all(request, id=2):
    people = Person.objects.all()
    years_wise = {}
    for p in people:
        if p.year not in years_wise.keys():
            years_wise[p.year] = []
        years_wise[p.year].append(p)
        if p.id == id:
            fp = p
    keys = []
    for i in years_wise.keys():
        keys.append(i)
    keys.sort(reverse=True)
    template = loader.get_template('diary/all.html')
    context = {
        'person':fp,
        'years':keys,
    }
    return HttpResponse(template.render(context, request))