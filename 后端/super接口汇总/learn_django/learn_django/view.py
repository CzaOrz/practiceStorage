import json

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, render, HttpResponseRedirect, resolve_url


def api_01(request): return HttpResponse('hello world, this is api-01')


def api_02(request, multi_path=None):
    return HttpResponse(f'hello world, this is api-02, and multi_path is {multi_path}')


def api_03(request):
    print(request.GET.keys())  # dict_keys
    print(request.GET.values())  # generator
    print(request.GET.items())  # generator
    return HttpResponse(f"hello, this is api-03, and the params is {dict(request.GET.items())}", status=200)


def api_04(request):
    if request.method == 'POST':
        print(request.POST.items())  # generator
        return JsonResponse({
            'status': 1,
            'form': dict(request.POST.items()),
        },
            json_dumps_params={'ensure_ascii': False})


def api_05(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode())
        return JsonResponse({'status': 1, 'form': json_data}, json_dumps_params={'ensure_ascii': False})


def api_06(request):
    cookies = request.COOKIES
    return JsonResponse({'status': 1, 'cookies': cookies}, json_dumps_params={'ensure_ascii': False})


def api_07(request): return api_06(request)


def api_08(request):
    raise Http404("hello, this is api-08")


def api_09(request):
    return render(request, 'errors/error_404.html',
                  {'error_text': 'whats fuck?', 'error_code': '10086'},
                  status=404)


def api_10(request):
    if request.method == 'POST':
        raise Http404("hello, this is api-08")
    else:
        return api_08(request)


def api_11(request):
    if request.method == 'POST':
        return JsonResponse({'status': 0, 'msg': 'Forbidden'}, status=403)
    else:
        return api_09(request)


def api_12(request):
    return render(request, 'test/index.html', {'remarks': 'he he'})
