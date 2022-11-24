from django.shortcuts import render

# Create your views here.
def todView(request):

    return render(request,'todoList/index.html')