from django.db import models


# Create your models here.

# -----------------------------------------班级表--------------------------------
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    first_day = models.DateField()

    def __str__(self):
        return self.cname

    class Meta:
        db_table = "class"


# -----------------------------------------学生表--------------------------------

class Student(models.Model):
    id = models.AutoField(primary_key=True)  # id 可以不写 自动创建，作为主键
    sname = models.CharField(max_length=48)
    cid = models.ForeignKey(to="Class", to_field="id", on_delete=models.CASCADE, related_name="students")  # 关系到班级
    detail = models.OneToOneField("StudentDetail", on_delete=models.CASCADE)  # 一对一

    def __str__(self):
        return self.sname

    class Meta:
        db_table = "student"


class StudentDetail(models.Model):
    height = models.PositiveSmallIntegerField()  # 无符号整型
    memo = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "studentdetail"


# ------------------------------------------教师表----------------------------------

# 方法一（自己创建两张表）
# class Teacher(models.Model):
#     tname = models.CharField(max_length=32, null=True)
#
#     class Meta:
#         db_table = "teacher"
#
# class TechearToClass(models.Model):
#     t_id = models.ForeignKey(to="Teacher", on_delete=models.CASCADE)
#     cid = models.ForeignKey(to="Class")
#
#     class Meta:
#         unique_together = ("tid", "cid")

# 方法二：(ORM自动创建关联的两张表)
class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField("Class")

    class Meta:
        db_table = "teacher"


# # 方法三（推荐方法）
# class Teacher(models.Model):
#     tname = models.CharField(max_length=32)
#     cid = models.ManyToManyField(to="Class", through="TeacherToClass", through_fields=("tid", "cid"))
#
#
# class TeacherToClass(models.Model):
#     tid = models.ForeignKey(to="Teacher")
#     cid = models.ForeignKey(to="Class")
#
#     class Meta:
#         unique_together = ("tid", "cid")

#----------------------------------------------------------------------------------------------