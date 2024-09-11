from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'SHIP SHOP',
        'name': 'Nobel Julian Bintang (2306202826)',
        'class': 'PBP F',
    }

    return render(request, "main.html", context)