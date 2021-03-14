from django.shortcuts import render

posts = [
    {
        'title': 'Peter Pan goes to town',
        'author': 'Anri',
        'content': 'Peter just saw another family he wants to rob.',
        'date': '13 March 2021',
    },
    {
        'title': 'Santa goes to town',
        'author': 'Anri',
        'content': 'No more chimneys for olg grey. He now gives them out at the door.',
        'date': '14 March 2021',
    }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)  # template path


def about(request):
    return render(request, 'blog/about.html')
