# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'UserGallery', fields ['owner']
        db.delete_unique(u'galleries_usergallery', ['owner_id'])


        # Changing field 'UserGallery.owner'
        db.alter_column(u'galleries_usergallery', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['members.Member']))

    def backwards(self, orm):

        # Changing field 'UserGallery.owner'
        db.alter_column(u'galleries_usergallery', 'owner_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['members.Member']))
        # Adding unique constraint on 'UserGallery', fields ['owner']
        db.create_unique(u'galleries_usergallery', ['owner_id'])


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
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'member_images'", 'unique': 'True', 'null': 'True', 'to': u"orm['members.Member']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'galleries.usergallery': {
            'Meta': {'object_name': 'UserGallery', '_ormbases': [u'galleries.Gallery']},
            u'gallery_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.Gallery']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_galleries'", 'null': 'True', 'to': u"orm['members.Member']"})
        },
        u'galleries.userprivategallery': {
            'Meta': {'object_name': 'UserPrivateGallery', '_ormbases': [u'galleries.UserGallery']},
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'usergallery_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.UserGallery']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'galleries.userpublicgallery': {
            'Meta': {'object_name': 'UserPublicGallery', '_ormbases': [u'galleries.UserGallery']},
            u'usergallery_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.UserGallery']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'avatar_pic': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'disk_space_used': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_gallery': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['galleries.UserPublicGallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'register_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'})
        }
    }

    complete_apps = ['galleries']