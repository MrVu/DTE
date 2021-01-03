from .models import PageInfo


def page_info_proccessor(request):
    page_info = PageInfo.objects.first()
    return {'page_info': page_info}
