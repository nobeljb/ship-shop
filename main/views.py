from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306202826',
        'name': 'Nobel',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)