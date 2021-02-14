from .models import PageInfo, Article, CustomerComment


def page_info_proccessor(request):
    page_info = PageInfo.objects.first()
    return {'page_info': page_info}

def articles_processor(request):
    articles = Article.objects.filter(show_on_homepage=True).order_by('-date')[:3]
    return {'articles': articles}
