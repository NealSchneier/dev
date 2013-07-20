from django.db import models, connection

# Create your models here.

class Brand(models.Model):
	name = models.CharField(max_length=30)
	recognition = models.CharField(max_length=200)
	rating = models.IntegerField()
	details = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class Bluetooth(models.Model):
	ver3 = models.CharField(max_length=1)
	ver4 = models.CharField(max_length=1)
	rating = models.IntegerField()
	details = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.ver3 + " " + self.ver4

class ScreenType(models.Model):
	name = models.CharField(max_length=20)
	rating = models.IntegerField()
	details = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class Resolution(models.Model):
	first = models.IntegerField()
	second = models.IntegerField()
	dpi = models.IntegerField()
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return str(self.dpi)

class Screen(models.Model):
	name = models.CharField(max_length=20)
	screen_type = models.ForeignKey(ScreenType)
	brand = models.ForeignKey(Brand)
	sensitivity = models.IntegerField()
	speed = models.IntegerField()
	resolution = models.ForeignKey(Resolution)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.name
	
class Battery(models.Model):
	name = models.CharField(max_length=100)
	brand_id = models.ForeignKey(Brand)
	talk_time = models.IntegerField()
	internet_time = models.IntegerField()
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class OS_Family(models.Model):
	family = models.CharField(max_length=20)
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.family

class OS(models.Model):
	name = models.CharField(max_length=20)
	family = models.ForeignKey(OS_Family)
	version = models.CharField(max_length=50)
	feature1 = models.CharField(max_length=100)
	feature2 = models.CharField(max_length=100)
	feature3 = models.CharField(max_length=100)	
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Camera(models.Model):
	megapixels = models.DecimalField(max_digits=10, decimal_places=2)
	speed = models.IntegerField()
	flash = models.IntegerField()
	filters = models.IntegerField()
	software = models.IntegerField()
	front_facing = models.CharField(max_length=1)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return str(self.megapixels)

class Speakers(models.Model):
	location = models.CharField(max_length=100)
	amplifier = models.CharField(max_length=1)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.location

class Video(models.Model):
	hdmi = models.CharField(max_length=1)
	resolution = models.ForeignKey(Resolution)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.hdmi

class Keyboard(models.Model):
	physical = models.CharField(max_length=1)
	stylus = models.CharField(max_length=1)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return "Physical: " + self.physical + " Stylus: " + self.stylus

class Wireless(models.Model):
	ieee_n = models.CharField(max_length=1)
	ieee_g = models.CharField(max_length=1)
	rating = models.IntegerField()
	details = models.TextField(blank=True)
	
	def __unicode__(self):
		return "Wireless N: " + self.ieee_n + " Wireless G: " + self.ieee_g

class Processor(models.Model):
	name = models.CharField(max_length=20)
	cores = models.IntegerField()
	clock_speed = models.DecimalField(max_digits=10, decimal_places=2)
	rating = models.IntegerField()
	details = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class Speed(models.Model):
	processor = models.ForeignKey(Processor)
	ram = models.IntegerField()
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.processor.name
	
class UI(models.Model):
	name = models.CharField(max_length=20)
	brand = models.ForeignKey(Brand)
	version = models.CharField(max_length=20)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class App_Family(models.Model): #like Google Maps, Facebook and so on.
	name = models.CharField(max_length=20)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Apps(models.Model): #Specific Version of each app
	app_family = models.ForeignKey(App_Family)
	version = models.CharField(max_length=20)
	os = models.ForeignKey(OS)
	rating = models.IntegerField()
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.app_family.name + " Version: " + self.version

class Carrier(models.Model):
	name = models.CharField(max_length=20)
	LTE = models.CharField(max_length=1)
	percent_coverage = models.IntegerField() #percent of US with LTE
	details = models.TextField(blank=True)

	def __unicode__(self):
		return self.name
	
class Maps(models.Model):#
	turn_by_turn = models.CharField(max_length=1)
	maps = models.CharField(max_length=1)
	apps = models.ForeignKey(Apps)
	
	def __unicode__(self):
		return self.apps.app_family.name

class SmartphoneManager(models.Manager):
	def Smartphones(self):
		cursor = connection.cursor()
		cursor.execute(
			""" 
			SELECT shownerd_smartphone.name "name", shownerd_voice_recognition.name, shownerd_maps.name, shownerd_apps.name, shownerd_ui.name, shownerd_processor.name, shownerd_speed.ram, shownerd_wireless.ieee_n, shownerd_wireless.ieee_g, shownerd_keyboard.rating, shownerd_video.rating_id, shownerd_speakers.rating, shownerd_camera.rating, shownerd_os.name, shownerd_battery.name, shownerd_screen.rating, shownerd_bluetooth.rating, shownerd_brand.rating from shownerd_smartphone join shownerd_maps on (maps_id=shownerd_maps.id) join shownerd_voice_recognition on (voice_recognition_id = shownerd_voice_recognition.id) join shownerd_apps on (apps_id = shownerd_apps.id) join shownerd_ui on (ui_id = shownerd_ui.id) join shownerd_speed on (speed_id = shownerd_speed.id) join shownerd_processor on (shownerd_smartphone.processor_id = shownerd_processor.id) join shownerd_wireless on (wireless_id = shownerd_wireless.id) join shownerd_keyboard on (keyboard_id = shownerd_keyboard.id) join shownerd_video on (video_id = shownerd_video.id) join shownerd_speakers on (speakers_id = shownerd_speakers.id) join shownerd_camera on (camera_id = shownerd_camera.id) join shownerd_os on (os_id = shownerd_os.id) join shownerd_battery on (battery_id = shownerd_battery.id) join shownerd_screen on (screen_id = shownerd_screen.id) join shownerd_bluetooth on (bluetooth_id = shownerd_bluetooth.id) join shownerd_brand on (brand_id = shownerd_brand.id)		
		""")
		return cursor.fetchall()
	def Names(self):
		cursor = connection.cursor()
		cursor.execute(
			"""SELECT name from shownerd_smartphone""")
		return [row[0] for row in cursor.fetchone()]

class Smartphone(models.Model):
	name = models.CharField(max_length=20)
	maps = models.ForeignKey(Maps)
	ui = models.ForeignKey(UI)
	speed = models.ForeignKey(Speed)
	processor = models.ForeignKey(Processor)	
	wireless = models.ForeignKey(Wireless)
	keyboard = models.ForeignKey(Keyboard)
	video = models.ForeignKey(Video)
	speakers = models.ForeignKey(Speakers)
	camera = models.ForeignKey(Camera)
	os = models.ForeignKey(OS)
	battery = models.ForeignKey(Battery)
	screen = models.ForeignKey(Screen)
	bluetooth = models.ForeignKey(Bluetooth)
	brand = models.ForeignKey(Brand)	
	details = models.TextField(blank=True)
	rating = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class Smartphone_To_Apps_Family(models.Model):
	Smartphone = models.ForeignKey(Smartphone)
	app_family = models.ForeignKey(App_Family)

#need to create trigger for Smartphone_To_Apps_Family