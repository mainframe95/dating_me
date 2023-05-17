from tortoise.models import Model
from tortoise import fields
import uuid

class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
    participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')

    def __str__(self):
        return self.name


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name
    
    

class Admin(Model):
    id = fields.UUIDField(pk=True) 
    username = fields.CharField(max_length=60, null=True)
    firstname = fields.CharField(max_length=50, null= True)
    lastname = fields.CharField(max_length=50, null= True)
    email = fields.CharField(max_length=255)
    access = fields.CharField(max_length=255)
    pwd = fields.CharField(max_length=255, null=True)
    salt = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"Admin: #{self.id} -> {self.username}, {self.username} {self.lastname}"

    
    
class Gender(Model):
    # id = fields.IntField(pk=True)
    id = fields.UUIDField(pk=True) 
    label = fields.CharField(max_length=10)
    is_actived = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.label
    
    


class Member(Model):
    # id = fields.IntField(pk=True)
    id = fields.UUIDField(pk=True) 
    username = fields.CharField(max_length=60, null=True)
    firstname = fields.CharField(max_length=50, null= True)
    lastname = fields.CharField(max_length=50, null= True)
    email = fields.CharField(max_length=255)
    tel = fields.CharField(max_length=20)
    gender = fields.ForeignKeyField('models.Gender', related_name='gender')
    pwd = fields.CharField(max_length=255, null=True)
    salt = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f" Member: #{self.id} -> {self.username}, {self.username} {self.lastname}"
    

class HangOn(Model):
    id = fields.UUIDField(pk=True) 
    first_member = fields.ForeignKeyField(
        "models.Member", verbose_name=("first_member"),
        related_name='first_member')
    second_member = fields.ForeignKeyField(
        "models.Member", verbose_name=("second_member"),
        related_name='second_member')
    is_actived = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    