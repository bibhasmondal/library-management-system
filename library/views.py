from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Book, Subject
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .forms import *
from django.contrib import messages
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime

# Create your views here.

"""class Subject(CreateView):
    model = Subject
    fields = ['title','code']

class BookCreate(CreateView):
    model = Book
    fields = ['author', 'title', 'subject', 'image']

class BookEdit(UpdateView):
    model = Book
    fields = ['author', 'title', 'subject', 'image']"""


class BookIndex(generic.ListView):
    template_name = 'library/index.html'
    context_object_list = 'object_list'

    def get_queryset(self):
        return Book.objects.all()


def BookDetail(request, id):
    reqbook = get_object_or_404(Book, id=id)
    if request.method == 'GET':
        form = BookRequest(None)
        return render(request, 'library/detail.html', {'form': form, 'reqbook': reqbook})
    if request.method == 'POST' and request.user.is_authenticated:
        form = BookRequest(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.book = reqbook  # adding current book to the request.
            req.save()
            if reqbook.issued == True:
                messages.warning(
                    request, 'This book has already been issued out,')
            messages.success(request, 'Your request for ' + reqbook.title + ' has been registered.')
        return render(request, 'library/detail.html', {'form': form, 'reqbook': reqbook})


def NewForm(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid():
            form.save()
            message.success(request, 'Your request has been submitted.')
    else:
        form = New(None)
    return render(request, 'library/new.html', {'form': form})


class BookAdd(CreateView):
    template_name = 'library/add.html'
    form_class = BookAdd


class BookEdit(UpdateView):
    model = Book
    template_name = 'library/edit_book.html'
    fields = ['title', 'author', 'subject', 'publisher', 'image']


@login_required
def IssueBook(request, id):
    req = get_object_or_404(Request, id=id)
    book = req.book
    if not request.user.is_staff:
        messages.warning(request, 'You aren\'t authorized to issue. Please contact a librarian.')
        return redirect('library:home')
    if not book.issued:
        book.issued = True
        book.issued_name = req.user
        book.save()
        req.status = True
        req.issued_by = request.user
        req.issue_date = date.today()
        req.save()
        messages.success(
            request, 'You issued out this book to ' + req.user.first_name + '.')
        return redirect('library:admin_dash')
    else:
        messages.error(
            request, 'Oops! Something went wrong! Looks like this book was already issued.')
    return redirect('library:admin_dash')

@login_required
def ReturnBook(request, id):
    req = get_object_or_404(Request, id=id)
    book = req.book
    if not (book.issued and (req.user==request.user or request.user.is_staff)):
        messages.warning(
            request, 'It doesn\'t look like this book had been issued out to you. Contact an admin.')
    req.retstatus = True
    req.return_request_date = date.today()
    req.save()
    messages.success(request, 'You asked for this book to be collected.')
    return redirect('library:user_dashboard')

@login_required
def CollectBook(request, id):
    req = get_object_or_404(Request, id=id)
    book = req.book
    if not request.user.is_staff:
        messages.warning(request, 'You aren\'t authorized to collect. Please contact a librarian.')
        return redirect('library:home')
    if not book.issued:
        messages.warning(
            request, 'It doesn\'t look like this book had been issued out. Contact an admin.')
    else:
        book.issued = False
        book.save()
        req.status = False
        req.returned_by = request.user
        req.return_date = date.today()
        req.save()
        messages.success(request, 'You collected this book.')
    return redirect('library:admin_dash')


def UndoReturn(request, id):
    req = get_object_or_404(Request, id=id)
    req.retstatus = False
    req.save()
    messages.success(request, "This return was cancelled.")
    return redirect('library:user_dashboard')


import re
import operator


def Search(request):
    if request.GET.get('q'):
        global query
        message = "you submitted " + request.GET['q']
        query = request.GET['q']
        q = query.lower()
        q = re.split('\s|\,', q)
        q = [x for x in q if x]
        all_books = Book.objects.all()
        results = []
        for book in all_books:
            slug = book.author.lower() + '-' + book.title.lower() + '-' + \
                book.subject.title.lower() + '-' + book.publisher.lower()
            # results.append(slug)
            count = 0
            for tag in q:
                if tag in slug:
                    count += 1
            if count == len(q):
                thisresult = [book, count]
                results.append(thisresult)
        results.sort(key=operator.itemgetter(1), reverse=True)
        message += str(q)
        message += str(results)

    else:
        message = "Nothing submitted!"
        results = []
        eresults = []
        query = ''

    return render(request, 'library/search.html', {'message': message, 'query': query, 'results': results})


# def FindEbooks(string):
#   httpslibgen.io/search.php?req=bachelor of arts&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def

def LibHome(request):
    return render(request, 'library/library.html')

@login_required
def UserDashboard(request):
    """View for library dashboard of individual, non-librarian user."""

    context = {}

    my_requests = Request.objects.filter(user = request.user)
    context['all'] = my_requests
    context['req_00'] = my_requests.filter(status=0, retstatus=0)
    context['req_01'] = my_requests.filter(status=0, retstatus=1)
    context['req_11'] = my_requests.filter(status=1, retstatus=1)
    context['req_10'] = my_requests.filter(status=1, retstatus=0)

    # context['req_01'] = context['req_01'].filter(self.due_date()>datetime.datetime.today())

    return render(request, 'library/user_dashboard.html', context)

def deleteRequest(request, id):
    """View to delete a request if it is archived or requested, only."""

    r = get_object_or_404(Request, id=id)
    if (request.user.is_staff or r.user == request.user) and r.status==False and r.retstatus==False:
        Request.objects.get(id=id).delete()
        messages.success(request, "Request successfully cancelled.")
    else:
        messages.error(request, "You may not permission to delete that request.")
    return redirect('library:user_dashboard')

@login_required
def adminDash(request):
    """Dashboard for librarian."""

    r = Request.objects.all()
    req_00 = r.filter(status=0, retstatus=0)
    req_01 = r.filter(status=0, retstatus=1)
    req_10 = r.filter(status=1, retstatus=0)
    req_11 = r.filter(status=1, retstatus=1)

    # req_pending = req_00.filter(book__issued==False)
    # ret_overdue = req_10.filter(due_date() < datetime.today())

    context = {
        # 'requests': req_pending,
        # 'overdue': ret_overdue,
        # 'returns': req_11
        'req_00': req_00,
        'req_01': req_01,
        'req_10': req_10,
        'req_11': req_11,
    }

    return render(request, 'library/dashboard.html', context)
