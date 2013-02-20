# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageModel'
        db.create_table(u'galleries_imagemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('owner', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('filesize', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'galleries', ['ImageModel'])

        # Adding model 'Gallery'
        db.create_table(u'galleries_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
        ))
        db.send_create_signal(u'galleries', ['Gallery'])

        # Adding M2M table for field photos on 'Gallery'
        db.create_table(u'galleries_gallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm[u'galleries.gallery'], null=False)),
            ('imagemodel', models.ForeignKey(orm[u'galleries.imagemodel'], null=False))
        ))
        db.create_unique(u'galleries_gallery_photos', ['gallery_id', 'imagemodel_id'])

        # Adding model 'UserGallery'
        db.create_table(u'galleries_usergallery', (
            (u'gallery_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['galleries.Gallery'], unique=True, primary_key=True)),
            ('user_test', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'galleries', ['UserGallery'])

        # Adding model 'UserPublicGallery'
        db.create_table(u'galleries_userpublicgallery', (
            (u'usergallery_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['galleries.UserGallery'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'galleries', ['UserPublicGallery'])

        # Adding model 'UserPrivateGallery'
        db.create_table(u'galleries_userprivategallery', (
            (u'usergallery_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['galleries.UserGallery'], unique=True, primary_key=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'galleries', ['UserPrivateGallery'])


    def backwards(self, orm):
        # Deleting model 'ImageModel'
        db.delete_table(u'galleries_imagemodel')

        # Deleting model 'Gallery'
        db.delete_table(u'galleries_gallery')

        # Removing M2M table for field photos on 'Gallery'
        db.delete_table('galleries_gallery_photos')

        # Deleting model 'UserGallery'
        db.delete_table(u'galleries_usergallery')

        # Deleting model 'UserPublicGallery'
        db.delete_table(u'galleries_userpublicgallery')

        # Deleting model 'UserPrivateGallery'
        db.delete_table(u'galleries_userprivategallery')


    models = {
        u'galleries.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'linked_galleries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['galleries.ImageModel']"}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'galleries.imagemodel': {
            'Meta': {'object_name': 'ImageModel'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'filesize': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'owner': ('django.db.models.fields.IntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'galleries.usergallery': {
            'Meta': {'object_name': 'UserGallery', '_ormbases': [u'galleries.Gallery']},
            u'gallery_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.Gallery']", 'unique': 'True', 'primary_key': 'True'}),
            'user_test': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'galleries.userprivategallery': {
            'Meta': {'object_name': 'UserPrivateGallery', '_ormbases': [u'galleries.UserGallery']},
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'usergallery_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.UserGallery']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'galleries.userpublicgallery': {
            'Meta': {'object_name': 'UserPublicGallery', '_ormbases': [u'galleries.UserGallery']},
            u'usergallery_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.UserGallery']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['galleries']