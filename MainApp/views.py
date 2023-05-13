from django.http import Http404
from django.shortcuts import render, redirect
from .models import Snippet
from .forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def log_in(request):
    return render(request, 'users/log_in.html')

def password_change(request):
    return render(request, 'accounts/password_change/form.html')


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request, 'add_snippet.html', {'form': form})


def create_snippet(request):
   if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("redirect_url")
       return render(request,'add_snippet.html',{'form': form})


def create_snippet(request):
   form = SnippetForm()
   return render(request, 'add_snippet.html', {'form': form})


def index_page(request):
    context = {'pagename': 'PythonBin',
               #'posts': Post.objects.all(),
               }
    return render(request, 'pages/index.html', context)

def snippet_page(request,id):
    try:
        snippet = Snippet.objects.get(pk=id)
        return render(request, 'pages/snippet_page.html', {'snippet': snippet})
    except ObjectDoesNotExist:
        raise Http404(f'Товар с id = {id} не найден')


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'snippets': snippets,
        "count": len(snippets)
    }
    return render(request, 'pages/view_snippets.html', context)

