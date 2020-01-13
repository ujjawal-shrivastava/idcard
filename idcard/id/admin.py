from django.contrib import admin
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter, RelatedDropdownFilter
from .models import Student
from django.contrib.auth.models import Group

admin.site.unregister(Group)

def IncrementYear(modeladmin, request, queryset):
    for obj in queryset:
        if (obj.year<3):     
            obj.year += 1
            obj.save()
        else:
            continue
IncrementYear.short_description = "Increment year for selected students"

def DecrementYear(modeladmin, request, queryset):
    for obj in queryset:
        if (obj.year>1):     
            obj.year -= 1
            obj.save()
        else:
            continue
DecrementYear.short_description = "Decrement year for selected students"



class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll', 'name', 'course','year','image_tag_list','date_of_birth')
    list_display_links = ('roll', 'name')
    list_editable =()
    
    list_filter = (
        ('course', ChoiceDropdownFilter),    
        ('year', ChoiceDropdownFilter),
        ('blood_group', ChoiceDropdownFilter),
    )
    filter_horizontal =()
    search_fields =('name','roll','course','email')
    readonly_fields = ('image_tag',)

    actions =[IncrementYear,DecrementYear]

admin.site.register(Student, StudentAdmin)



