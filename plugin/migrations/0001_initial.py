# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClickTrack'
        db.create_table('plugin_clicktrack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('clicks', self.gf('django.db.models.fields.IntegerField')(max_length=7)),
        ))
        db.send_create_signal('plugin', ['ClickTrack'])

    def backwards(self, orm):
        # Deleting model 'ClickTrack'
        db.delete_table('plugin_clicktrack')

    models = {
        'plugin.clicktrack': {
            'Meta': {'object_name': 'ClickTrack'},
            'clicks': ('django.db.models.fields.IntegerField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['plugin']