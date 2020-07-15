from django.shortcuts import render
from django.http import HttpResponse

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit_md(request):
    return render(request,"encyclopedia/edit.html")

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

