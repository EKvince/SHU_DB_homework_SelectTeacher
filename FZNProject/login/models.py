# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comments(models.Model):
    sno = models.CharField(db_column='Sno', max_length=10)  # Field name made lowercase.
    tno = models.CharField(db_column='Tno', max_length=10)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comments'


class SMajor(models.Model):
    mno = models.IntegerField(db_column='Mno', primary_key=True)  # Field name made lowercase.
    mtext = models.CharField(db_column='Mtext', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_major'


class St(models.Model):
    sno = models.CharField(db_column='Sno', max_length=10)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=10)  # Field name made lowercase.
    tno = models.CharField(db_column='Tno', max_length=10)  # Field name made lowercase.
    tname = models.CharField(db_column='Tname', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'st'


class Student(models.Model):
    sno = models.CharField(db_column='Sno', primary_key=True, max_length=10)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=10)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2)  # Field name made lowercase.
    mno = models.IntegerField(db_column='Mno')  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    tno = models.CharField(db_column='Tno', primary_key=True, max_length=10)  # Field name made lowercase.
    tname = models.CharField(db_column='Tname', max_length=10)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2)  # Field name made lowercase.
    pro = models.CharField(db_column='Pro', max_length=30)  # Field name made lowercase.
    number = models.IntegerField()
    contact = models.CharField(db_column='Contact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    d_information = models.CharField(db_column='D_information', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'
