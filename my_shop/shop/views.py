from django.shortcuts import render

# Create your views here.
def func1(request):
    return render(request, 'shop/index.html', {})
def func2(request):
    return render(request, 'shop/index1.html', {})
def func3(request):
    return render(request, 'shop/index2.html', {})

