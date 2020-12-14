from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Urls, History
from .serializers import HistorySerializer

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def change_url(request, url, original):
    is_same_url = Urls.objects.filter(edit=url)
    if is_same_url:
        historydata = History(content=is_same_url[0].original)
        historydata.save()
        return Response(is_same_url[0].encoding)
    else:
        BASE56 = '123456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
        arr = []
        # fasten code
        arr_append = arr.append
        _divmod = divmod
        base = 56
        num = len(Urls.objects.all()) + 1
        print("idx: ",num)
        while num and len(arr) < 8:
            num, rem = _divmod(num, base)
            print(num, rem)
            arr_append(BASE56[rem])
        arr.reverse()
        shortened = ''.join(arr)
        if 'dbslh' in original:
            if 'www.' in original:
                original = original.replace('dbslhwww.', '')
            else:
                original = original.replace('dbslh', '')
        while 'slh' in original:
            original = original.replace('slh', '/')
        while 'pcent' in original:
            original = original.replace('pcent', '%')
        while 'quesm' in original:
            original = original.replace('quesm', '?')
        print("changed: ",original)
        urldata = Urls(original=original, edit=url, encoding=shortened)
        urldata.save()
        historydata = History(content=original)
        historydata.save()
        return Response(shortened)

@api_view(['GET'])
def url_redirect(request, url):
    find_url = Urls.objects.get(encoding=url)
    original = find_url.original
    return Response(original)

@api_view(['GET'])
def get_history(request):
    history = History.objects.all()[::-1]
    print(history)
    serializer = HistorySerializer(history, many=True)
    return Response(serializer.data)