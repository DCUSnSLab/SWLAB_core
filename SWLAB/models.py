from django.db import models

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

class Semester(models.Model):
    semestername = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()

class User(models.Model):
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    number = models.CharField(max_length=30)
    gittoken = models.CharField(max_length=30, null=True)
    DEPARTMENT = [
        (1, "컴퓨터소프트웨어학부"),
        (2, "기타 등등")
    ]
    department = models.CharField(default=1, choices=DEPARTMENT, max_length=30)

class Lecture(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True)
    year = models.IntegerField()
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL)
    type = models.ForeignKey(LecType, on_delete=models.SET_NULL, null=True)

class Lecturer(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    isallow = models.BooleanField(default=False)