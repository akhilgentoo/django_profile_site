from django.contrib import admin
from .models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt


# Register your models here.


class aboutpage_admin(admin.ModelAdmin):
    list_display = ("description",)
    search_display = ("description",)
    filter_display = ("description",)  
admin.site.register(aboutpage,aboutpage_admin)

class Hobbies_admin(admin.ModelAdmin):
    list_display = ("hb1","hb2","hb3","hb4")
    search_display = ("hb1","hb2","hb3","hb4")
    filter_display = ("hb1","hb2","hb3","hb4")   
admin.site.register(Hobbies1,Hobbies_admin)



class Education_category_admin(admin.ModelAdmin):
    list_display = ("ed1","ed2","ed3","ed4")
    search_display = ("ed1","ed2","ed3","ed4")
    filter_display = ("ed1","ed2","ed3","ed4")   
admin.site.register(Education_category1,Education_category_admin)


class Education_category_details_admin(admin.ModelAdmin):
    list_display = ("ed1_details","ed2_details","ed3_details","ed4_details")
    search_display = ("ed1_details","ed2_details","ed3_details","ed4_details")
    filter_display = ("ed1_details","ed2_details","ed3_details","ed4_details")   
admin.site.register(Education_category_details1,Education_category_details_admin)


class skills1_admin(admin.ModelAdmin):
    list_display = ("skill1_description","sk1","sk2","sk3","sk4","sk5","sk6","sk7","sk8","sk9","sk10")
    search_display = ("skill1_description","sk1","sk2","sk3","sk4","sk5","sk6","sk7","sk8","sk9","sk10")
    filter_display = ("skill1_description","sk1","sk2","sk3","sk4","sk5","sk6","sk7","sk8","sk9","sk10")   
admin.site.register(skills1,skills1_admin)


class Experience_admin(admin.ModelAdmin):
    list_display = ("exp1_sub","exp1_desc","exp2_sub","exp2_desc","exp3_sub","exp3_desc","exp4_sub","exp4_desc","exp5_sub","exp5_desc","exp6_sub","exp6_desc","exp7_sub","exp7_desc")
    search_display = ("exp1_sub","exp1_desc","exp2_sub","exp2_desc","exp3_sub","exp3_desc","exp4_sub","exp4_desc","exp5_sub","exp5_desc","exp6_sub","exp6_desc","exp7_sub","exp7_desc")
    filter_display = ("exp1_sub","exp1_desc","exp2_sub","exp2_desc","exp3_sub","exp3_desc","exp4_sub","exp4_desc","exp5_sub","exp5_desc","exp6_sub","exp6_desc","exp7_sub","exp7_desc")  
admin.site.register(Experience1,Experience_admin)
    
