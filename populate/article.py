from populate import base
from article.models import Article, Comment

titles = ['如何考試100分','10分鐘到我家', '簡單學abc']
comments = ['很好', '棒棒喔', '別裝死']

def populate():
    print('this is populate/article.py', end='')
    Article.objects.all().delete()
    Comment.objects.all().delete()

    for title in titles:
        article = Article()
        article.title = title
        for j in range(20):
            article.content += title + '\n'
        article.save()
        for comment in comments:
            Comment.objects.create(article=article, content=comment)
    print('done')

if __name__=='__main__':
    populate()
