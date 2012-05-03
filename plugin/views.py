# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from plugin.models import ClickTrack

import json

def widget(request):

    if 'page_id' in request.GET:
        page_id = request.GET['page_id']
        if ClickTrack.objects.filter(page_id=page_id):
            clicks = ClickTrack.objects.get(page_id=page_id).clicks
        else:
            clicks = 0
    else:
        page_id = 'no account'
        clicks = 0

    data = render_to_string('widget.js', {
        'name': 'John Back',
        'page_id': page_id,
        'clicks': clicks,
    })

    response = HttpResponse(data, content_type='text/javascript')

    return response

def home(request):

    ctx = RequestContext(request, {

	})

    return render_to_response('home.html', context_instance=ctx)

@csrf_exempt
def click(request, page_id):

    if request.method == 'POST':
        if ClickTrack.objects.filter(page_id=page_id).exists():
            track = ClickTrack.objects.get(page_id=page_id)
            track.add_click()
        else:
            track = ClickTrack.objects.create(page_id=page_id, clicks=1)

        data = json.dumps({'clicks': track.clicks })

        response = HttpResponse(data, content_type='application/json')

        return response

    return HttpResponseBadRequest('This page is not directly accessible')