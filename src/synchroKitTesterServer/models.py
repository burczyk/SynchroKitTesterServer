from django.db import models
from datetime import datetime

class User(models.Model):
    name        = models.CharField(max_length=200)
    birthDate   = models.DateField()
    
    def save(self):
        super(User,self).save()
        try:
            lastUpdateDate = UpdateDate.objects.get(pk='User')
        except UpdateDate.DoesNotExist:
            lastUpdateDate = UpdateDate()
            lastUpdateDate.className = 'User'
            
        lastUpdateDate.updateDate = datetime.now()
        UpdateDate.save(lastUpdateDate)
        
    def __unicode__(self):
        return unicode(self.name)
        

class Message(models.Model):
    user    = models.ForeignKey(User)
    text    = models.CharField(max_length=32767)
    
    def save(self):
        super(Message,self).save()
        try:
            lastUpdateDate = UpdateDate.objects.get(pk='Message')
        except UpdateDate.DoesNotExist:
            lastUpdateDate = UpdateDate()
            lastUpdateDate.className = 'Message'
            
        lastUpdateDate.updateDate = datetime.now()
        UpdateDate.save(lastUpdateDate)    

class UpdateDate(models.Model):
    className   = models.CharField(max_length=255, primary_key=True)
    updateDate  = models.DateTimeField()     
    
    def __unicode__(self):
        return unicode(self.className)
