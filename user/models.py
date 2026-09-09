from django.db import models

# Create your models here.
#tbl_batch
class tbl_batch(models.Model):
    batch_name=models.CharField(max_length=50,null=True)
    added_date=models.DateField(null=True)
    def __str__(self):
        return self.batch_name

#tblcontact
class tblcontact(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=50,null=True)
    message=models.TextField(null=True)

#tblgallery
class tblgallery(models.Model):
    title=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="static/picture/",null=True)

#tblteam
class tblteam(models.Model):
    name=models.CharField(max_length=200,null=True)
    designation=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="static/team/",null=True)

#tbl_register
class tbl_register(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True)
    profile_picture=models.ImageField(upload_to="static/profile/",null=True)
    user_batch=models.ForeignKey(tbl_batch,on_delete=models.SET_NULL,null=True,blank=True)

#tbl_upcomingbatch
class tbl_upcomingbatch(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    batchname=models.CharField(max_length=100,null=True)
    batch_picture=models.ImageField(upload_to="static/batch/",null=True)
    starting_date=models.DateField(null=True)

#tbl_category
class tbl_category(models.Model):
    category=models.CharField(max_length=100,null=True)
    category_picture=models.ImageField(upload_to="static/category/",null=True)
    batch=models.ForeignKey(tbl_batch,on_delete=models.CASCADE,null=True)
    def __str__(self):
            return f"{self.category} - {self.batch.batch_name}"

#tbl_lectures
class tbl_lectures(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    video_title=models.TextField(null=True)
    video_description=models.TextField(null=True)
    video_link=models.CharField(max_length=200,null=True)
    added_date=models.DateField(null=True)

#tbl_softwarekit
class tbl_software(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    picture=models.ImageField(upload_to="static/software/",null=True)
    download_link=models.CharField(max_length=300,null=True)

#tbl_live
class tbl_live(models.Model):
    title=models.CharField(max_length=200,null=True)
    batch=models.ForeignKey(tbl_batch,on_delete=models.CASCADE)
    description=models.TextField(null=True)
    time=models.CharField(max_length=30,null=True)
    date=models.DateField(null=True)
    joining_link=models.TextField(null=True)
    picture=models.ImageField(upload_to="static/liveclass/",null=True)

#tbl_task
class tbl_task(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    batch=models.ForeignKey(tbl_batch,on_delete=models.CASCADE)
    marks=models.IntegerField(null=True)
    task_file=models.FileField(upload_to="static/task/",null=True)
    added_date=models.DateField(null=True)

#tbl_notes
class tbl_notes(models.Model):
    title=models.CharField(max_length=300,null=True)
    description=models.TextField(null=True)
    batch=models.ForeignKey(tbl_batch,on_delete=models.CASCADE)
    notes_file=models.FileField(upload_to="static/notes/",null=True)
    added_date=models.DateField(null=True)