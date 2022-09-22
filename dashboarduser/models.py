from django.db import models

# Create your models here.

class Dashboard(models.Model):
    """
    Profile model added here
    """
    title = models.CharField(max_length=100)
    postDate = models.DateField()
    description = models.CharField(max_length=500) 
    venue = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100)
    isInternal = models.CharField(max_length=1,default='Y')
    image = models.CharField(max_length=500)    
   
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        
    def __str__(self):
        return "{}".format(self.title)
     

