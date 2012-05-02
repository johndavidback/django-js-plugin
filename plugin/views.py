# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

def widget(request):

	data = render_to_string('widget.js')

	response = HttpResponse(data, content_type='text/javascript')

	return response

def home(request):

	ctx = RequestContext(request, {

	})

	return render_to_response('home.html', context_instance=ctx)