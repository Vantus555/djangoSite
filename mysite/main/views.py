import io
import os
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import *

from .models import *
# Create your views here.


class index(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
        context['books'] = Book.objects.all()

        if 'id' in request.GET:
            cat = Categories.objects.get(id=request.GET['id'])
            context['books'] = Book.objects.filter(categories=cat)
        else:
            context['books'] = Book.objects.all()
        return render(request, "main/index.html", context=context)


class login(View):
    def get(self, request):
        context = {'form': LoginForm}
        return render(request, "main/reg/loginForm.html", context=context)

    def post(self, request):
        user = LoginForm(request.POST)

        if user.is_valid():
            request.session.set_expiry(3600 * 24 * 30)
            request.session['login'] = request.POST['name']
            return HttpResponseRedirect("/")
        else:
            context = {}
            context['form'] = user
            return render(request, "main/login.html", context=context)


class logout(View):
    def get(self, request):
        if 'login' in request.session:
            request.session.flush()
        return HttpResponseRedirect("/")


class reg(View):
    def get(self, request):
        context = {'form': RegForm}
        return render(request, "main/reg/regForm.html", context=context)

    def post(self, request):
        user = RegForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect("/login")
        else:
            context = {'form': user}
            return render(request, "main/reg/regForm.html", context=context)


class profile(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
            context['user'] = MyUsers.objects.get(
                name=request.session['login'])
            context['books'] = context['user'].books.all()
            return render(request, "main/profile.html", context=context)
        else:
            return HttpResponseRedirect("/")


class addbook(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
            context['form'] = BookForm
            return render(request, "main/addBookForm.html", context=context)
        else:
            return HttpResponseRedirect("/")

    def post(self, request):
        context = {}
        user = BookForm(request.POST, request.FILES)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect("/")
        else:
            context = {'form': user}
            return render(request, "main/addBookForm.html", context=context)


class addcategories(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
            context['form'] = CategoriesForm
            return render(request, "main/addCategory.html", context=context)
        else:
            return HttpResponseRedirect("/")

    def post(self, request):
        user = CategoriesForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect("/")
        else:
            context = {'form': user}
            return render(request, "main/reg/addCategory.html", context=context)


class viewBook(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
            context['book'] = Book.objects.get(id=request.GET['id'])

            file_path = os.path.join(settings.MEDIA_ROOT,
                                     str(context['book'].file).replace('/', '\\'))

            with io.open(file_path, mode="r", encoding="utf-8") as file:
                context['text'] = file.read()

        return render(request, "main/readBook.html", context=context)


class viewCategories(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']

        context['categories'] = Categories.objects.all()

        return render(request, "main/categories.html", context=context)


class info(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']

        return render(request, "main/info.html", context=context)


class addBookMe(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
            user = MyUsers.objects.get(
                name=request.session['login'])

            book = Book.objects.get(id=request.GET['id'])
            user.books.add(book)
            # user.books

        return HttpResponseRedirect("/")


class deleteBookMe(View):
    def get(self, request):
        context = {}
        if 'login' in request.session:
            context['name'] = request.session['login']
            user = MyUsers.objects.get(
                name=request.session['login'])

            book = Book.objects.get(id=request.GET['id'])
            user.books.remove(book)
            # user.books

        return HttpResponseRedirect("/profile")
