# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Brand'
        db.create_table(u'shownerd_brand', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recognition', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'shownerd', ['Brand'])

        # Adding model 'Bluetooth'
        db.create_table(u'shownerd_bluetooth', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('ver3', self.gf('django.db.models.fields.CharField')(max_length=1)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ver4', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'shownerd', ['Bluetooth'])

        # Adding model 'ScreenType'
        db.create_table(u'shownerd_screentype', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['ScreenType'])

        # Adding model 'Resolution'
        db.create_table(u'shownerd_resolution', (
            ('second', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'shownerd', ['Resolution'])

        # Adding model 'Screen'
        db.create_table(u'shownerd_screen', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sensitivity', self.gf('django.db.models.fields.IntegerField')()),
            ('brand_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Brand'])),
            ('resolution_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Resolution'])),
            ('screen_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.ScreenType'])),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'shownerd', ['Screen'])

        # Adding model 'Battery'
        db.create_table(u'shownerd_battery', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('talk_time', self.gf('django.db.models.fields.IntegerField')()),
            ('brand_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Brand'])),
            ('internet_time', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'shownerd', ['Battery'])

        # Adding model 'OS'
        db.create_table(u'shownerd_os', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('feature2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('family', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('feature1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature3', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'shownerd', ['OS'])

        # Adding model 'Camera'
        db.create_table(u'shownerd_camera', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('megapixels', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('flash', self.gf('django.db.models.fields.IntegerField')()),
            ('front_facing', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('filters', self.gf('django.db.models.fields.IntegerField')()),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('software', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'shownerd', ['Camera'])

        # Adding model 'Speakers'
        db.create_table(u'shownerd_speakers', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'shownerd', ['Speakers'])

        # Adding model 'Video'
        db.create_table(u'shownerd_video', (
            ('rating_id', self.gf('django.db.models.fields.IntegerField')()),
            ('resolution_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Resolution'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hdmi', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'shownerd', ['Video'])

        # Adding model 'Keyboard'
        db.create_table(u'shownerd_keyboard', (
            ('stylus', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('physical', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'shownerd', ['Keyboard'])

        # Adding model 'Wireless'
        db.create_table(u'shownerd_wireless', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('ieee_g', self.gf('django.db.models.fields.CharField')(max_length=1)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ieee_n', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'shownerd', ['Wireless'])

        # Adding model 'Processor'
        db.create_table(u'shownerd_processor', (
            ('cores', self.gf('django.db.models.fields.IntegerField')()),
            ('clock_speed', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['Processor'])

        # Adding model 'Speed'
        db.create_table(u'shownerd_speed', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('ram', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Processor'])),
        ))
        db.send_create_signal(u'shownerd', ['Speed'])

        # Adding model 'UI'
        db.create_table(u'shownerd_ui', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['UI'])

        # Adding model 'Apps'
        db.create_table(u'shownerd_apps', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['Apps'])

        # Adding model 'Carrier'
        db.create_table(u'shownerd_carrier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('LTE', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['Carrier'])

        # Adding model 'Maps'
        db.create_table(u'shownerd_maps', (
            ('maps', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('turn_by_turn', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['Maps'])

        # Adding model 'Voice_Recognition'
        db.create_table(u'shownerd_voice_recognition', (
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'shownerd', ['Voice_Recognition'])

        # Adding model 'Smartphone'
        db.create_table(u'shownerd_smartphone', (
            ('speakers', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Speakers'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('voice_recognition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Voice_Recognition'])),
            ('battery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Battery'])),
            ('os', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.OS'])),
            ('screen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Screen'])),
            ('apps', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Apps'])),
            ('processor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Processor'])),
            ('wireless', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Wireless'])),
            ('maps', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Maps'])),
            ('camera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Camera'])),
            ('ui', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.UI'])),
            ('keyboard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Keyboard'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Video'])),
            ('bluetooth', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Bluetooth'])),
            ('speed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Speed'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shownerd.Brand'])),
        ))
        db.send_create_signal(u'shownerd', ['Smartphone'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Brand'
        db.delete_table(u'shownerd_brand')

        # Deleting model 'Bluetooth'
        db.delete_table(u'shownerd_bluetooth')

        # Deleting model 'ScreenType'
        db.delete_table(u'shownerd_screentype')

        # Deleting model 'Resolution'
        db.delete_table(u'shownerd_resolution')

        # Deleting model 'Screen'
        db.delete_table(u'shownerd_screen')

        # Deleting model 'Battery'
        db.delete_table(u'shownerd_battery')

        # Deleting model 'OS'
        db.delete_table(u'shownerd_os')

        # Deleting model 'Camera'
        db.delete_table(u'shownerd_camera')

        # Deleting model 'Speakers'
        db.delete_table(u'shownerd_speakers')

        # Deleting model 'Video'
        db.delete_table(u'shownerd_video')

        # Deleting model 'Keyboard'
        db.delete_table(u'shownerd_keyboard')

        # Deleting model 'Wireless'
        db.delete_table(u'shownerd_wireless')

        # Deleting model 'Processor'
        db.delete_table(u'shownerd_processor')

        # Deleting model 'Speed'
        db.delete_table(u'shownerd_speed')

        # Deleting model 'UI'
        db.delete_table(u'shownerd_ui')

        # Deleting model 'Apps'
        db.delete_table(u'shownerd_apps')

        # Deleting model 'Carrier'
        db.delete_table(u'shownerd_carrier')

        # Deleting model 'Maps'
        db.delete_table(u'shownerd_maps')

        # Deleting model 'Voice_Recognition'
        db.delete_table(u'shownerd_voice_recognition')

        # Deleting model 'Smartphone'
        db.delete_table(u'shownerd_smartphone')
    
    
    models = {
        u'shownerd.apps': {
            'Meta': {'object_name': 'Apps'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.battery': {
            'Meta': {'object_name': 'Battery'},
            'brand_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Brand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_time': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'talk_time': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.bluetooth': {
            'Meta': {'object_name': 'Bluetooth'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'ver3': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ver4': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'shownerd.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'recognition': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'shownerd.camera': {
            'Meta': {'object_name': 'Camera'},
            'filters': ('django.db.models.fields.IntegerField', [], {}),
            'flash': ('django.db.models.fields.IntegerField', [], {}),
            'front_facing': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'megapixels': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'software': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.carrier': {
            'LTE': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'Meta': {'object_name': 'Carrier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'shownerd.keyboard': {
            'Meta': {'object_name': 'Keyboard'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'physical': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'stylus': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'shownerd.maps': {
            'Meta': {'object_name': 'Maps'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'turn_by_turn': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'shownerd.os': {
            'Meta': {'object_name': 'OS'},
            'family': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'feature2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'feature3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'shownerd.processor': {
            'Meta': {'object_name': 'Processor'},
            'clock_speed': ('django.db.models.fields.IntegerField', [], {}),
            'cores': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.resolution': {
            'Meta': {'object_name': 'Resolution'},
            'first': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.screen': {
            'Meta': {'object_name': 'Screen'},
            'brand_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Brand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'resolution_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Resolution']"}),
            'screen_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.ScreenType']"}),
            'sensitivity': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.screentype': {
            'Meta': {'object_name': 'ScreenType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.smartphone': {
            'Meta': {'object_name': 'Smartphone'},
            'apps': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Apps']"}),
            'battery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Battery']"}),
            'bluetooth': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Bluetooth']"}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Brand']"}),
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Camera']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyboard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Keyboard']"}),
            'maps': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Maps']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'os': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.OS']"}),
            'processor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Processor']"}),
            'screen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Screen']"}),
            'speakers': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Speakers']"}),
            'speed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Speed']"}),
            'ui': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.UI']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Video']"}),
            'voice_recognition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Voice_Recognition']"}),
            'wireless': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Wireless']"})
        },
        u'shownerd.speakers': {
            'Meta': {'object_name': 'Speakers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.speed': {
            'Meta': {'object_name': 'Speed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Processor']"}),
            'ram': ('django.db.models.fields.IntegerField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.ui': {
            'Meta': {'object_name': 'UI'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'shownerd.video': {
            'Meta': {'object_name': 'Video'},
            'hdmi': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating_id': ('django.db.models.fields.IntegerField', [], {}),
            'resolution_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shownerd.Resolution']"})
        },
        u'shownerd.voice_recognition': {
            'Meta': {'object_name': 'Voice_Recognition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shownerd.wireless': {
            'Meta': {'object_name': 'Wireless'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ieee_g': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ieee_n': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['shownerd']
