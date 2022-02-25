# from second_app.models import Student
from second_app.models import *
# from django.contrib.auth.models import User

# exec(open("C:\\Users\\Lenovo\\Desktop\\aniket\\b6\\Django\\first_project\\second_app\\db_shell.py").read())


# data = Student.objects.all()
# print(data)
# first_object = Student.objects.first()
# print(first_object , type(first_object))

# print(first_object.name)

# data = Student.objects.filter(id__gte=3)
# for i in data:
#     print(i.__dict__)
# print(data)
# print(data.query)

# data = Student.objects.get(id=2)
# print(data)

# data = Student.objects.filter(name__startswith = "A")
# print(data)
# print(data.get_stud_by_name_startwith())

# data = Student.objects.exclude(name__startswith = "A")
# print(data)
# try:
#     single_data = Student.objects.get(id= 5)
    # single_data.get_stu_details()
    # single_data.get_avg_marks()
    # single_data.delete()
    # single_data.name = "ddd"
    # single_data.save()
    # print(single_data)
# except Student.DoesNotExist:
#     print("No Data")

# def increment_marks():
#     all_data = Student.objects.all()
#     for stud in all_data:
#         stud.marks += (stud.marks *(5/100))
#         stud.save()

# increment_marks()

# object create

# ----admin_page

# stud = Student(name= "HHH", age= 18, marks= 86)
# stud.save()

# stud_2 = Student.objects.create(name= "Aniket", age= 23, marks= 98)
# print(stud_2)

# stud = Student.get_active_stud()
# print(stud)

# stud = Student.get_Inactive_stud()
# print(stud)

# print(Student.active_object.all())

# active_stud = Student.active_object.all()
# print(active_stud)

# inactive_stud = Student.inactive_object.all()
# print(inactive_stud)


# res = Student.get_avg_marks_by_lambda()
# print(res)


# stud = Student.get_stud_by_name_startwith()
# print(stud)


# stud = Student.get_stud_by_name_excluding_A_startwith()
# print(stud)

# stud = Student.creat_student()
# print(stud)
# stud.save()

# stud= Student.increment_marks()
# print(stud)
# stud.save()


# data = Student.insert_data_in_table
# print(data)

# deta = Student.delete_stud()
# print(deta)

# data = Student.creat_student()
# print(data.__dict__)
# for i in stud:
#     print(i)

# data = Student.read_from_databases
# print(data)

# data = Student.read_from_databases()
# print(data)



# data = Student.read_from_database
# print(data)
# for i in data:
#     print(i.__dict__)
    # print(f"""------------------------------
    # ---------Student_ID :- {data[0]}--------
    # ---------Student_Name:-{data[1]}---------
    # ---------Student_age :- {data[2]}--------
    # ---------Student_is_active :- {data[3]}---
    # ----------------------------------------""")

# data = Student.get_avg_marks_by_lambda()
# print(data)
# data.save()
# for i in data:
#     print(i)

# data = Student.get_stud_details()
# print(data)


# all_data = Student.objects.all()
# # print(all_data)
# for data in all_data:
#     print(data , end=" , ")

# data = User.objects.all()
# print(data[0])

#------------------------------------------------------------------------------

# s1 = Student.objects.all().order_by("name")
# print(s1)

# s1 = Student.objects.all().order_by("-name")
# print(s1)

#---clg---principal----dept---student----subject


#----collage se principal


try:
    c1 = Collage.objects.get(name = "Dy Patil")
    # c1 = Collage.objects.get(name = "H.V.P.M.")
except Collage.DoesNotExist:
    print("collage does not exit.....!")
else:
    print(c1)

# print(c1.principal)
# print(dir(c1))

#------one to many 

# print(c1.dpartment_set.all()[0])
# print(c1.dpartment_set.all())

#----department se all student--------

# s1 = Dpartment.objects.get(name = "chemical")
# print(s1.student_set.all())
# print(dir(s1))

# s1 = Student.objects.get(name= "Aniket")  #----many to many
# print(dir(s1))
# print(s1)
# print(s1.subject_set.all())


dept = c1.dpartment_set.all().filter(name= "chemical")
# print(dir(dept))
stud = dept.student_set.all()
print(stud)




