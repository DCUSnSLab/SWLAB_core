from django.db import models

from account.models import User

class SubjectType(object):
    SUBJECT = 'subject'
    EXTRACURRICULAR = 'extracurricular'

class LectureType(models.Model):
    # TYPE = [
    #     (1, "코딩"),
    #     (2, "시스템"),
    #     (3, "프로젝트"),
    #     (4, "팀플")
    # ]
    name = models.CharField(max_length=20)
    desc = models.TextField(null=True)

class Lecture(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True)
    year = models.IntegerField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    semester = models.IntegerField()
    lectype = models.ForeignKey(LectureType, on_delete=models.CASCADE, null=True)
    subtype = models.TextField(default=SubjectType.SUBJECT)


    class Meta:
        db_table = "lecture"

class Lecturer(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    isallow = models.BooleanField(default=False)