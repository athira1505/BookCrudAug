from django.shortcuts import render
from django.views.generic import View
from store.forms import BookForm
from store.models import Book

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=BookForm()
        return render(request,"book_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=BookForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)   #{'title': 'abc', 'author': 'pqr', 'price': 500, 'language': 'english', 'genre': 'novel', 'year': '2020'}


            Book.objects.create(
                title=data.get("title"),
                author=data.get("author"),
                price=data.get("price"),
                language=data.get("language"),
                genre=data.get("genre"),
                year=data.get("year")
                )

        return render(request,"book_add.html",{"form":form_instance})
