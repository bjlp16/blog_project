from django.shortcuts import render

# Create your views here.

def article(request):
    '''
    render the article page
    '''
    context = {'like':'Django article嘿嘿'}
    return render(request, 'article/article.html', context)