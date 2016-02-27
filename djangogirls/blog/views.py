from django.shortcuts import render

# Create your views here.
def func1(request):
    return render(request, 'blog/index.html', {})
def func2(request):
    return render(request, 'blog/index1.html', {})
def func3(request):
    return render(request, 'blog/index2.html', {})

