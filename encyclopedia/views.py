from django.shortcuts import render
from django.http import HttpResponse

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_redirect(request,name):
    page = name.lower()
    md = util.get_entry(page)
    if md is not None:
        html = markdown2.markdown(md)
        return render(request,"encyclopedia/page.html",{
            "page": html
        })
    else:
        return render(request,"encyclopedia/page.html",{
            "page": "Not found :c"
        })
