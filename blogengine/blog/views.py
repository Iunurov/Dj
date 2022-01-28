from django.shortcuts import render


# Create your views here.
def post_list(request):
    n = ['Oleg', 'Masha', 'Olja', 'Ksu']
    return render(request, 'blog/index.html', context={'names': n})