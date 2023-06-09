from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Registration(models.Model):
    First_name = models.CharField(max_length=200, null=True)
    Last_name = models.CharField(max_length=200, null=True)
    Email = models.EmailField(max_length=200, null=True)
    Password = models.CharField(max_length=200, null=True)
    Registration_date = models.DateField(auto_now_add=True, null=True)
    Num_of_courses_enrolled = models.IntegerField(default=0, null=True)
    Num_of_courses_completed = models.IntegerField(default=0, null=True)
    Qualification = models.TextField(null=True)
    Introduction_brief = models.TextField(null=True)
    Image = models.ImageField(upload_to='media', null=True)
    Num_of_enrolled_students = models.IntegerField(null=True)
    Average_review_rating = models.IntegerField(null=True)
    Num_of_reviews = models.IntegerField(null=True)
    About_website = models.TextField(null=True)
    User_role = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)

    #def __str__(self):
       # return self.First_name


class Subject(models.Model):
    Subject_title = models.CharField(max_length=200, null=True)
    Course_title = models.CharField(max_length=200, null=True)
    Course_brief = models.TextField(null=True)
    Course_duration = models.IntegerField(null=True)
    Num_of_chapters = models.IntegerField(null=True)
    Course_fee = models.FloatField(null=True)
    Language = models.CharField(max_length=200, null=True)
    Chapter_title = models.CharField(max_length=200, null=True)
    Num_of_assignments = models.IntegerField(null=True)
    Chapter_Content_name = models.ImageField(upload_to='media', null = True)
    Chapter_text_content = models.TextField(null=True)
    Chapter_Content_type = models.CharField(max_length=200,null=True)
    Chapter_Content_Is_mandatory = models.BooleanField(null=True)
    Chapter_Content_Time_required_in_sec = models.IntegerField(null=True)
    Chapter_Content_Is_open_for_free = models.BooleanField(null=True)
    Sub_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.Subject_title


class Enrollment(models.Model):
    Student_name = models.CharField(max_length=200,null=True)
    Student_email = models.EmailField(null=True)
    Subject_name = models.CharField(max_length=200, null=True)
    Course_name = models.CharField(max_length=200,null=True)
    Teacher_name = models.CharField(max_length=200, null=True)
    Teacher_email = models.EmailField(null=True)
    Attendance = models.IntegerField(null=True)
    Pending_days = models.IntegerField(null=True)
    Enrollment_date = models.DateField(auto_now_add=True, null=True)
    Teacher_response = models.CharField(max_length=200, null=True)
    Paid_amount = models.FloatField(null=True)
    Certificate = models.CharField(max_length=200, null=True)
    Is_paid_subscription = models.BooleanField(null=True)
    notify = models.CharField(max_length=200, null = True)
    enrol_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)


class Learning_progress(models.Model):
    Student_name = models.CharField(max_length=200, null=True)
    Student_email = models.EmailField(null=True)
    Subject_name = models.CharField(max_length=200, null=True)
    Course_name = models.CharField(max_length=200, null=True)
    Course_chapter_name = models.CharField(max_length=200, null=True)
    Course_chapter_content_name = models.ImageField(upload_to='media', null = True)
    Begin_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    Completion_timestamp = models.DateTimeField(auto_now=True, null=True)
    Status = models.CharField(max_length=200, null=True)
    Teacher_email = models.EmailField(max_length=200, null=True)
    Learn_p_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)


class Feedback(models.Model):
    Student_name = models.CharField(max_length=200, null=True)
    Student_email = models.EmailField(null=True)
    Teacher_name = models.CharField(max_length=200, null=True)
    Teacher_email = models.EmailField(null=True)
    Subject_name = models.CharField(max_length=200,null=True)
    Course_name = models.CharField(max_length=200, null=True)
    Rating_score = models.IntegerField(null=True)
    Feedback_text = models.TextField(default='Nil', null=True)
    Submission_date = models.DateField(null=True)
    Feed_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)


class Messages(models.Model):
    Category = models.CharField(max_length=200, null=True)
    Name = models.CharField(max_length=200,null=True )
    From_email = models.EmailField(null=True)
    To_email = models.EmailField(null=True)
    Message_content = models.TextField(default='Nil', null=True)


class Exam(models.Model):
    Student_name = models.CharField(max_length=200, null=True)
    Student_email = models.EmailField(null=True)
    Teacher_name = models.CharField(max_length=200, null=True)
    Subject_name = models.CharField(max_length=200, null=True)
    Course_name = models.CharField(max_length=200, null=True)
    Question = models.TextField(null=True)
    Option1 = models.TextField(null=True)
    Option2 = models.TextField(null=True)
    Option3 = models.TextField(null=True)
    Correct_answer = models.TextField(null=True)
    Lock = models.CharField(max_length=200, null=True)
    Time_start = models.DateTimeField(null=True)
    Time_stop = models.DateTimeField(null=True)
    Exam_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)


class Exam_results(models.Model):
    Student_name = models.CharField(max_length=200, null=True)
    Student_email = models.EmailField(max_length=200, null=True)
    Teacher_name = models.CharField(max_length=200, null=True)
    Subject_name = models.CharField(max_length=200, null=True)
    Total_marks = models.IntegerField(null=True)
    Acquired_marks = models.IntegerField(null=True)
    Grade = models.CharField(max_length=200, null=True)
    Time_stop = models.DateTimeField(auto_now=True, null=True)
    Exam_res_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)


class Blogs(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Blog_content = models.TextField(null=True)
    Image = models.ImageField(null=True)
    Date_blog = models.DateField(null=True)
    Approval_status = models.CharField(max_length=200, null=True)


class Requests(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Email = models.EmailField(null=True)
    User_category = models.CharField(max_length=200, null=True)
    Old_password = models.CharField(max_length=200, null=True)
    New_password = models.CharField(max_length=200, null=True)
    Req_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null = True)

