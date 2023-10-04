from django.db import models

from account.models import User


class LecType(models.Model):
    TYPE = [
        (1, "코딩"),
        (2, "시스템"),
        (3, "프로젝트"),
        (4, "팀플")
    ]
    name = models.CharField(
        max_length=20,
        choices=TYPE,
        default=1
    )
    SUBJECTTYPE = [
        (True, "교과"),
        (False, "비교과")
    ]
    subject = models.BooleanField(
        choices=SUBJECTTYPE,
        default=True
    )
    env = models.BinaryField(max_length=4, null=True)

class Lecture(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True)
    year = models.IntegerField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(LecType, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lecture"

class Lecturer(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    isallow = models.BooleanField(default=False)