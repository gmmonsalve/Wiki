from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from . import util
from django.urls import reverse
import markdown2


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
        redirect('index')
       


def page_redirect(request,name):
    md = util.get_entry(name)
    if md is not None:
        html = markdown2.markdown(md)
        return render(request,"encyclopedia/page.html",{
            "page": html,
            "title": name
        })
    else:
        return render(request,"encyclopedia/page.html",{
            "page": "<h1>Page Not found</h1>"
        })

def search(request):
    q = request.GET.get("q", None)
    if q:
        search = q
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