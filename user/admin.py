from django.contrib import admin
from .models import *

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("id","name","mobile","email","message")
admin.site.register(tblcontact,tblcontactAdmin)

class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)

class tblteamAdmin(admin.ModelAdmin):
    list_display=("id","name","designation","picture")
admin.site.register(tblteam,tblteamAdmin)

class tbl_registerAdmin(admin.ModelAdmin):
    list_display=("user_batch","name","mobile","password","email","address","profile_picture")
admin.site.register(tbl_register,tbl_registerAdmin)

class tbl_batchAdmin(admin.ModelAdmin):
    list_display=("id","batch_name","added_date")
admin.site.register(tbl_batch,tbl_batchAdmin)

class tbl_upcomingbatchAdmin(admin.ModelAdmin):
    list_display=("id","title","description","batchname","batch_picture","starting_date")
admin.site.register(tbl_upcomingbatch,tbl_upcomingbatchAdmin)

class tbl_categoryAdmin(admin.ModelAdmin):
    list_display=("id","batch","category","category_picture")
admin.site.register(tbl_category,tbl_categoryAdmin)

class tbl_lecturesAdmin(admin.ModelAdmin):
    list_display=("id","category","video_title","video_description","video_link","added_date")
admin.site.register(tbl_lectures,tbl_lecturesAdmin)

class tbl_softwareAdmin(admin.ModelAdmin):
    list_display=("id","title","description","picture","download_link")
admin.site.register(tbl_software,tbl_softwareAdmin)

class tbl_liveAdmin(admin.ModelAdmin):
    list_display=("id","title","batch","description","time","date","joining_link","picture")
admin.site.register(tbl_live,tbl_liveAdmin)

class tbl_taskAdmin(admin.ModelAdmin):
    list_display=("id","title","description","batch","marks","task_file","added_date")
admin.site.register(tbl_task,tbl_taskAdmin)

class tbl_notesAdmin(admin.ModelAdmin):
    list_display=("id","title","description","batch","notes_file","added_date")
admin.site.register(tbl_notes,tbl_notesAdmin)