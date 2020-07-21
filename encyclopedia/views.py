from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from . import util
from django.urls import reverse
from django.contrib import messages
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def edit(request,page):
    content = util.get_entry(page)
    return render(request,"encyclopedia/edit.html",{
        "title": page,
        "content": content
    })
   

def save_changes(request, page_name):
    content = request.POST.get("md", None)
    if content:
        util.save_entry(page_name,content)
        return redirect('page_redirect', name=page_name)
    else:
        return redirect('index')
       

def page_redirect(request,name):
    md = util.get_entry(name)
    if md:
        html = markdown2.markdown(md)
        return render(request,"encyclopedia/page.html",{
            "page": html,
            "title": name
        })
    else:
        return render(request,"encyclopedia/page.html",{
            "page": "<h1>Page Not found</h1>",
            "title": "Page not found",
            "empty": True
        })
   

def search(request):
    search = request.GET.get("q", None)
    if search:
        content = util.list_entries()
        result = [i for i in content if search.lower() in i.lower() or search.upper() in i.upper()] 
        print(result)
        if search in result:
             return redirect('page_redirect', name=search)
        else:
            return render(request, "encyclopedia/search.html",{
                "search": search,
                "entries": result
            })
    else:
        return redirect('index')


def create(request):
    title = request.POST.get("title",None)
    content = request.POST.get("entry",None)
    if title and content:
        if title in util.list_entries():
            messages.error(request, 'This entry already exists')
        else:
            util.save_entry(title,content)
            return redirect('page_redirect',name=title)
    return render(request,"encyclopedia/create.html")


def rand(request):
    random_entry = random.choice(util.list_entries())
    return redirect('page_redirect',name=random_entry)