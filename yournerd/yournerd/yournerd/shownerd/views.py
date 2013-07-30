from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from yournerd.shownerd.models import Smartphone

def brand(request):
	t = get_template("brand.html")
	html = t.render()
	return HttpResponse(html)

def Bluetooth(request):
	t = get_template("bluetooth.html")
	html = t.render()
	return HttpResponse(html)

def smartphones(request):
	t = get_template("smartphone.html")

	#needs to be updated to include the binding for the Smartphone_To_Apps_Family for each app_family
	smartphones = Smartphone.objects.raw('select shownerd_smartphone.id ' + 
		'from shownerd_smartphone join shownerd_maps on (shownerd_smartphone.maps_id = shownerd_maps.id) ' +
		'join shownerd_ui on (shownerd_smartphone.ui_id ' + 
		'= shownerd_ui.id) join shownerd_speed on (shownerd_smartphone.speed_id = shownerd_speed.id) join ' + 
		'shownerd_processor on (shownerd_smartphone.processor_id = shownerd_processor.id) join shownerd_wireless ' + 
		'on (shownerd_smartphone.wireless_id = shownerd_wireless.id) join shownerd_keyboard on ' + 
		'(shownerd_smartphone.keyboard_id = shownerd_keyboard.id) join shownerd_video on ' + 
		'(shownerd_smartphone.video_id = shownerd_video.id) join shownerd_speakers on ' + 
		'(shownerd_smartphone.speakers_id = shownerd_speakers.id) join shownerd_camera on (shownerd_smartphone.camera_id ' +
		'= shownerd_camera.id) join shownerd_os on (shownerd_smartphone.os_id = shownerd_os.id) ' + 
		'join shownerd_battery on (shownerd_smartphone.battery_id = shownerd_battery.id) join shownerd_screen  ' + 
		'on (shownerd_smartphone.screen_id = shownerd_screen.id) join shownerd_bluetooth on ' + 
		'(shownerd_smartphone.bluetooth_id = shownerd_bluetooth.id) join shownerd_brand on ' + 
		'(shownerd_smartphone.brand_id = shownerd_brand.id)')
	html = t.render(Context({'smartphones': smartphones}))
	return HttpResponse(html)
