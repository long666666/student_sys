from django.shortcuts import render, redirect, HttpResponse
from project import models
from django.urls import reverse


# Create your views here.
def class_list(request):
    class_list = models.Class.objects.all()
    return render(request, "class_list.html", locals())


# 删除班级
def delete_class(request):
    class_id = request.GET.get("class_id")
    models.Class.objects.filter(id=class_id).delete()
    return redirect(reverse("class_list"))  # reverse 反向解析


def add_class(request):
    if request.method == "POST":
        cname = request.POST.get("cname")
        first_day = request.POST.get("first_day")

        models.Class.objects.create(cname=cname, first_day=first_day)
        return redirect(reverse("class_list"))

    return render(request, "add_class.html")


def edit_class(request, arg):
    if request.method == "POST":
        id = request.POST.get("id")
        cname = request.POST.get("cname")
        first_day = request.POST.get("first_day")
        print(cname, first_day)

        # class_obj = models.Class.objects.get(id=id)
        # class_obj.cname = cname
        # class_obj.first_day = first_day
        # class_obj.save()
        models.Class.objects.filter(id=id).update(cname=cname, first_day=first_day)

        return redirect(reverse("class_list"))

    class_info = models.Class.objects.get(id=arg)
    class_list = models.Class.objects.all()

    return render(request, "edit_class.html", locals())


# --------------------------------------------学生------------------------------------------------------
def student_list(request):
    student_list = models.Student.objects.all()

    return render(request, "student_list.html", locals())


def add_student(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        cid = request.POST.get("cid")
        height = request.POST.get("height")
        memo = request.POST.get("memo")
        # print(sname, cid, height, memo)

        # 先进行StudentDetail数据的上传
        models.StudentDetail.objects.create(height=height, memo=memo)

        # 获取刚创建内容的id 用于创建学生表
        cid_id = models.StudentDetail.objects.last().id

        models.Student.objects.create(sname=sname, cid_id=cid, detail_id=cid_id)
        return redirect(reverse("student_list"))

    class_list = models.Class.objects.all()

    return render(request, "add_student.html", locals())


def delete_student(request):
    student_id = request.GET.get("student_id")
    detail_id = models.Student.objects.get(id=student_id).detail_id

    models.Student.objects.get(id=student_id).delete()

    models.StudentDetail.objects.get(id=detail_id).delete()

    return redirect(reverse("student_list"))


def edit_student(request, arg):
    if request.method == "POST":
        sid = request.POST.get("id")
        sname = request.POST.get("sname")
        cid = request.POST.get("cid")

        height = request.POST.get("height")
        memo = request.POST.get("memo")
        detail_id = models.Student.objects.get(id=sid).detail_id
        models.Student.objects.filter(id=sid).update(sname=sname, cid_id=cid, detail_id=detail_id)
        models.StudentDetail.objects.filter(id=detail_id).update(height=height, memo=memo)

        return redirect(reverse("student_list"))

    student_info = models.Student.objects.get(id=arg)
    class_list = models.Class.objects.all()

    detail_id = models.Student.objects.get(id=arg).detail_id
    detail = models.StudentDetail.objects.get(id=detail_id)

    return render(request, "edit_student.html", locals())


def teacher_list(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, "teacher_list.html", locals())


def delete_teacher(request, tid):
    models.Teacher.objects.filter(id=tid).delete()
    return redirect(reverse("teacher_list"))


def add_teacher(request):
    if request.method == "POST":
        tname = request.POST.get("tname")
        class_ids = request.POST.getlist("cid")
        print(tname, class_ids)

        teacher_obj = models.Teacher.objects.create(tname=tname)
        teacher_obj.cid.add(*class_ids)
        return redirect(reverse("teacher_list"))

    class_list = models.Class.objects.all()
    return render(request, "add_teacher.html", locals())


def edit_teacher(request, tid):
    # 获取老师对象
    teacher_obj = models.Teacher.objects.get(id=tid)

    if request.method == "POST":
        tname = request.POST.get("tname")
        class_id = request.POST.getlist("cid")

        # 更新老师信息
        teacher_obj.tname=tname
        teacher_obj.cid.set(class_id)
        teacher_obj.save()
        return redirect(reverse("teacher_list"))

    class_list = models.Class.objects.all()
    return render(request, "edit_teacher.html", locals())


def school(request):
    return render(request, "school.html")
