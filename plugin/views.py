# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

def widget(request):

	if 'account_id' in request.GET:
		account_id = request.GET['account_id']
	else:
		account_id = 'No account'

	data = render_to_string('widget.js', {
		'name': 'John Back',
		'account_id': account_id,
	})

	response = HttpResponse(data, content_type='text/javascript')

	return response

def home(request):

	ctx = RequestContext(request, {

	})

	return render_to_response('home.html', context_instance=ctx)