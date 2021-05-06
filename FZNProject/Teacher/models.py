# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comments(models.Model):
    sno = models.CharField(db_column='Sno', max_length=10)  # Field name made lowercase.
    tno = models.CharField(db_column='Tno', max_length=10)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LoginUser(models.Model):
    account = models.CharField(db_column='Account', unique=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login_user'


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
