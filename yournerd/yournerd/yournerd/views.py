from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import datetime


def hello(request):
	return HttpResponse("Htest")

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>Int %s hours, it will be %s</body></html>" % (offset, dt)
	return HttpResponse(html)
