from django.db import models

class UserInformation(models.Model):
    nickname = models.CharField(max_length=200)
    send_date = models.DateTimeField('nickname/email sent')
    platform = models.CharField(max_length=10) 
    def __str__(self):
        return self.platform + ': ' + self.nickname
    


