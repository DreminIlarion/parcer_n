from django.db import models

# Create your models here.
# class DataParser(models.Model):
#     description = models.TextField(blank=True, null=True, db_index=True)
#     price = models.IntegerField(blank=True, null=True)
#     area = models.IntegerField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'data_parser'
    

class Komerc(models.Model):
    # id = models.AutoField(primary_key=True)
    # is_checked = models.BooleanField(default=False,null=True, db_index=True)
    information = models.TextField(blank=True, null=True, db_index=True)
    price = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    datas = models.DateTimeField(blank=True, null=True)
    url = models.TextField(unique=True, blank=True, null=True)
    category = models.TextField(unique=True, blank=True, null=True)
    cadastral_number = models.TextField(unique=True, blank=True, null=True)
    photo = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'komerc'
        # ordering = ['-pk']

    def __str__(self):
        return self.information
    
# class Category(models.Model):
#     name = models.CharField(max_length=30,db_index=True)

#     def __str__(self):
#         return self.name
    
