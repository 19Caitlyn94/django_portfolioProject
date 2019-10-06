from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='images/')
    
    def summary(self):
        if len(self.body) > 100: 
            return self.body[:100] + "..."
        return self.body  
    
    def pub_date_formatted(self):
        return self.pub_date.strftime('%b %e %Y')