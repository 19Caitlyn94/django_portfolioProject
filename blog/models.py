from django.db import models

# Create your models here.

class Blog(models.Model):
    BUSINESS = 'Business'
    WORK = 'Work'
    STUDY = 'Study'
    OTHER = 'Other'

    LABEL_CHOICES = [
        (BUSINESS, 'Business'),
        (WORK, 'Work'),
        (STUDY, 'Study'),
        (OTHER, 'Other')
    ]

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='images/')
    label = models.CharField(
        max_length=20,
        choices=LABEL_CHOICES,
        default=OTHER,
    ) 

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 100: 
            return self.body[:100] + "..."
        return self.body  
    
    def pub_date_formatted(self):
        return self.pub_date.strftime('%b %e %Y')