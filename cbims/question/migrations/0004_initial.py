# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SingleChoiceQuestion'
        db.create_table(u'question_singlechoicequestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('right_choice', self.gf('django.db.models.fields.IntegerField')()),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('question', ['SingleChoiceQuestion'])

        # Adding M2M table for field clause_related on 'SingleChoiceQuestion'
        m2m_table_name = db.shorten_name(u'question_singlechoicequestion_clause_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('singlechoicequestion', models.ForeignKey(orm['question.singlechoicequestion'], null=False)),
            ('clause', models.ForeignKey(orm['regulation.clause'], null=False))
        ))
        db.create_unique(m2m_table_name, ['singlechoicequestion_id', 'clause_id'])

        # Adding model 'Choice'
        db.create_table(u'question_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['question.SingleChoiceQuestion'])),
            ('title', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('question', ['Choice'])

        # Adding model 'Question'
        db.create_table(u'question_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('discipline', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('like', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dislike', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.User'], null=True, blank=True)),
            ('last_modify', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('submit_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('wrong_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('source', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('question', ['Question'])

        # Adding M2M table for field tags on 'Question'
        m2m_table_name = db.shorten_name(u'question_question_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['question.question'], null=False)),
            ('tag', models.ForeignKey(orm['website.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'SingleChoiceQuestion'
        db.delete_table(u'question_singlechoicequestion')

        # Removing M2M table for field clause_related on 'SingleChoiceQuestion'
        db.delete_table(db.shorten_name(u'question_singlechoicequestion_clause_related'))

        # Deleting model 'Choice'
        db.delete_table(u'question_choice')

        # Deleting model 'Question'
        db.delete_table(u'question_question')

        # Removing M2M table for field tags on 'Question'
        db.delete_table(db.shorten_name(u'question_question_tags'))


    models = {
        'account.institute': {
            'Meta': {'object_name': 'Institute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'account.user': {
            'Meta': {'object_name': 'User'},
            'answered_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avatar_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Institute']", 'null': 'True', 'blank': 'True'}),
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_login_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "u'\\u5317\\u4eac'", 'max_length': '50', 'blank': 'True'}),
            'qq': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'upload_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'question.choice': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['question.SingleChoiceQuestion']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.IntegerField', [], {})
        },
        'question.question': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Question'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.User']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'discipline': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dislike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modify': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'source': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'submit_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'wrong_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'question.singlechoicequestion': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SingleChoiceQuestion'},
            'clause_related': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['regulation.Clause']", 'symmetrical': 'False', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_choice': ('django.db.models.fields.IntegerField', [], {})
        },
        'regulation.chapter': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Chapter'},
            'code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['regulation.Regulation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'regulation.clause': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Clause'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'creater': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first'", 'to': "orm['account.User']"}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_mandatory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_editor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'last'", 'to': "orm['account.User']"}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['regulation.Section']"})
        },
        'regulation.regulation': {
            'Meta': {'ordering': "('serial_number',)", 'object_name': 'Regulation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'regulation.section': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Section'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['regulation.Chapter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.tag': {
            'Meta': {'ordering': "('tag_type', 'order', 'name')", 'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fans': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.User']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Tag']", 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['question']