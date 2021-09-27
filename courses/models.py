from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "courses_courses"

class Sections(models.Model):
    title = models.CharField(max_length=100)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "courses_sections"

class Lectures(models.Model):
    title = models.CharField(max_length=100)
    sections = models.ForeignKey(Sections, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "courses_lectures"