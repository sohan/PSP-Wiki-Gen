from django.shortcuts import render_to_response
from pspgenwiki.models import WikiForm 
from django.http import HttpResponse
from django.template import RequestContext
from make_wiki import MakeWiki

def index(request):
    if request.method == 'POST':
        form = WikiForm(request.POST)
        if form.is_valid():
            return HttpResponse('form submitted successfully')
    else:
        form = WikiForm()

    return render_to_response('index.html', 
        {'form': form,},
        context_instance = RequestContext(request))

def make_wiki(wiki_form):
    wiki = MakeWiki()
    wiki.login(wiki_form['username'], wiki_form['password'])
    wiki.make_template(wiki_form['name'])
    pass
