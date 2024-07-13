from django.db import models

# Create your models here.

class aboutpage(models.Model):
    description =  models.TextField()
    
    def __str__(self):
        return self.description
    
class Hobbies1(models.Model):
    hb1 = models.CharField(max_length=500)
    hb2 = models.CharField(max_length=500)
    hb3 = models.CharField(max_length=500)
    hb4 = models.CharField(max_length=500)

    
    def __str__(self):
        return self.hb1
    

class Education_category1(models.Model): # This have details description
    ed1 = models.CharField(max_length=500)
    ed2 = models.CharField(max_length=500)
    ed3 = models.CharField(max_length=500)
    ed4 = models.CharField(max_length=500)

  
    def __str__(self):
        return self.ed1
    
    
class Education_category_details1(models.Model): # This have  just category
    ed1_details = models.CharField(max_length=500)
    ed2_details = models.CharField(max_length=500)
    ed3_details = models.CharField(max_length=500)
    ed4_details = models.CharField(max_length=500)

  
    def __str__(self):
        return self.ed1_details
    

class skills1(models.Model):
    skill1_description = models.TextField()
    sk1 = models.CharField(max_length=500)
    sk1_percentage = models.CharField(max_length=500)
    sk2 = models.CharField(max_length=500)
    sk2_percentage = models.CharField(max_length=500)
    sk3 = models.CharField(max_length=500)
    sk3_percentage = models.CharField(max_length=500)
    sk4 = models.CharField(max_length=500)
    sk4_percentage = models.CharField(max_length=500)
    sk5 = models.CharField(max_length=500)
    sk5_percentage = models.CharField(max_length=500)
    sk6 = models.CharField(max_length=500)
    sk6_percentage = models.CharField(max_length=500)
    sk7 = models.CharField(max_length=500)
    sk7_percentage = models.CharField(max_length=500)
    sk8 = models.CharField(max_length=500)
    sk8_percentage = models.CharField(max_length=500)
    sk9 = models.CharField(max_length=500)
    sk9_percentage = models.CharField(max_length=500)
    sk10 = models.CharField(max_length=500)
    sk10_percentage = models.CharField(max_length=500)

    
    def __str__(self):
        return self.sk1
    

class Experience1(models.Model):
    
    exp1_sub = models.CharField(max_length=500)
    exp1_desc = models.TextField()
    exp1_year = models.CharField(max_length=500)
    exp2_sub = models.CharField(max_length=500)
    exp2_desc = models.TextField()
    exp2_year = models.CharField(max_length=500)
    exp3_sub = models.CharField(max_length=500)
    exp3_desc = models.TextField()
    exp3_year = models.CharField(max_length=500)
    exp4_sub = models.CharField(max_length=500)
    exp4_desc = models.TextField()
    exp4_year = models.CharField(max_length=500)
    exp5_sub = models.CharField(max_length=500)
    exp5_desc = models.TextField()
    exp5_year = models.CharField(max_length=500)
    exp6_sub = models.CharField(max_length=500)
    exp6_desc = models.TextField()
    exp6_year = models.CharField(max_length=500)
    exp7_sub = models.CharField(max_length=500)
    exp7_desc = models.TextField()    
    exp7_year = models.CharField(max_length=500)

    def __str__(self):
        return self.exp1_sub