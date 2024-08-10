from django.shortcuts import get_object_or_404, render
from .models import MainContent
# from .models import ExistProduct

def index(request):

    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)
def detail(request, content_id):

    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)

# def exist_detail(request, exist_id):
#
#     content_list = get_object_or_404(ExistProduct, pk=exist_id)
#     context = {'content_list': content_list}
#     return render(request, 'pages/exist_detail.html', context)