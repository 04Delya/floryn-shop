from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245586',
        'name': 'Delya Ardiyanti',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)