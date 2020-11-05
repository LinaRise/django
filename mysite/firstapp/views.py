from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Post
from .models import Students
from .forms import PostForm
from django.shortcuts import redirect
from .filters import PostFilter


# Create your views here.

def post_list(request):
    return render(request, 'firstapp/post_list.html', {})


def about(request):
    return render(request, 'firstapp/about.html', {})


def index(request):
    qs = Post.objects.all()
    title_contains_query = request.GET.get('title_contains')
    print(title_contains_query)

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)
    context = {
        'queryset': qs
    }
    return render(request, 'firstapp/index.html', {"text": qs})


def addPost(request):
    return render(request, 'firstapp/addPost.html', {})


def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'firstapp/new.html', {'form': form})


# получение данных из бд
def indexStudents(request):
    students = Students.objects.all()
    return render(request, "firstapp/indexStudents.html", {"students": students})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        student = Students()
        student.group = request.POST.get("group")
        student.lastname = request.POST.get("lastname")
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.interests = request.POST.get("interests")
        student.save()
    return HttpResponseRedirect("/students/")


# изменение данных в бд
def edit(request, id):
    try:
        student = Students.objects.get(id=id)

        if request.method == "POST":
            student.group = request.POST.get("group")
            student.lastname = request.POST.get("lastname")
            student.name = request.POST.get("name")
            student.age = request.POST.get("age")
            student.interests = request.POST.get("interests")
            student.save()
            return HttpResponseRedirect("/students/")
        else:
            return render(request, "firstapp/edit.html", {"student": student})
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        student = Students.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect("/students/")
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
# def filterView(request):
#     qs = Post.objects.all()
#     title_contains_query = request.GET.get('title_contains')
#     print(title_contains_query)
#
#     if title_contains_query != '' and title_contains_query is not None:
#         qs = qs.filter(title__icontains=title_contains_query)
#     context = {
#         'queryset': qs
#     }
#     return render(request, 'firstapp/index.html', {"text": qs})
