from django.shortcuts import render

def index(request):
    # context = {
    #     'message': 'Hello World!'
    # }
    return render(request, 'djapp/index.html')