from audioop import avg
from audioop import avg
from functools import reduce
from os import name
from pickletools import markobject
from random import random

from django.db import models
from first_project.settings import DATABASES
import random
from django.db import connection


# Create your models here.

# id , name , marks, age 

class ActiveStudManager(models.Manager):
    def get_queryset(self):
        return super(ActiveStudManager, self).get_queryset().filter(is_active= 1)


class InactiveManager(models.Manager):
    def get_queryset(self):
        return super(InactiveManager, self).get_queryset().filter(is_active = 0)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.FloatField()
    is_active= models.BooleanField(default=1)
    active_object = ActiveStudManager()
    inactive_object = InactiveManager()
    objects = models.Manager()
    

    class Meta:
        db_table = "Student"

    def __str__(self) :
        return self.name

    @classmethod
    def increment_marks(cls):
        all_data = cls.objects.all()
        for stud in all_data:
            stud.marks += (stud.marks *(5/100))
            return stud
        

    @classmethod
    def get_active_stud(cls):
        all_active_student= Student.objects.filter(is_active=1)
        return all_active_student


    @classmethod
    def get_Inactive_stud(cls):
        all_active_student= Student.objects.filter(is_active=0)
        return all_active_student


    @classmethod
    def creat_student(cls):
        for i in range(1,11):
            stud = cls.objects.create(name= chr(64 +i), age= random.randint(20, 26) , marks= random.randint(68,98))
            return stud
        

    def get_stu_details(self):
        print(f"""--Student Id :- {self.id}
        Student Name :- {self.name}
        Student age :-{self.age}
        Student Marks :- {self.marks}
        ---""")

    @classmethod
    def get_stud_details(cls):
        all_data = cls.objects.all()
        for stud in all_data:
            print(f"""---------Student Id :- {stud.id}---------
            -------------------Student Name:- {stud.name}-------
            ------------------Student Age :- {stud.age}--------
            ------------------Student Marks :- {stud.marks}-----
            ----------------------------------------------------""")



    @classmethod
    def get_stud_by_name_startwith(cls):
        name = cls.objects.filter(name__startswith = "A")
        return name

    @classmethod
    def get_stud_by_name_excluding_A_startwith(cls):
        name = cls.objects.exclude(name__startswith = "A")
        return name

    @classmethod
    def delete_stud(cls):
        data = cls.objects.filter(id = 1).delete()
        print(data)


    @classmethod
    def get_avg_marks(cls):
        all_data = cls.objects.all()
        total = 0
        for i in all_data:
            total += i.marks
        avg = total/len(all_data)
        return avg

    @classmethod
    def get_avg_marks_by_lambda(cls):
        all_data = cls.objects.all()
        l = []
        for data in all_data:
            l.append(data.marks)
            avg_marks = reduce(lambda a, b : a +b , l) //len(l)
        return(avg_marks)

    
    def insert_data_in_table():                                   #-------------------get the memori address not inserted data sir---------------<function Student.insert_data_in_table at 0x000001EC8A3B5820>
        conn= DATABASES("second_app")
        insert_data_query = " insert into prod_info (name , age , marks, is_active) values ('gita',32, 84, 1)"
        conn_channel= conn.cursor()
        conn_channel.execute(insert_data_query)
        conn.commit()

    # def read_from_database():                                  #----------------same not show data in out put only location-----------<function Student.read_from_database at 0x0000015698CBCF70>
    #     conn = DATABASES("second_app")
    #     read_data_query = "select * from student"
    #     conn_channel = conn.cursor()
    #     conn_channel.execute(read_data_query)
    #     read_data = conn_channel.fetchall()
    #     return read_data

    
    # def read_from_databases():
    #     cursor = connection.cursor()
    #     cursor.execute('''SELECT count(*) FROM student''')
    #     row = cursor.fetchone()
    #     for i in row:
    #         print(i.name)


#--------------------------------------------------------------------------------


     #---------------Django relationship-----------------------


class Common_field(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Collage(Common_field):
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "collage"

#-----one to one--------

class Principal(Common_field):
    Collage = models.OneToOneField(Collage , on_delete =models.CASCADE, null= True)

    class Meta :
        db_table = "princi"

#---one to many-----

class Dpartment(Common_field):
    Collage = models.ForeignKey(Collage, on_delete= models.CASCADE , null= True)

    class Meta:
        db_table = "dept"

class Student(Common_field):
    marks = models.FloatField()
    is_active = models.BooleanField(default= True)
    Dpartment = models.ForeignKey(Collage, on_delete=models.SET_NULL, null= True)

    class Meta:
        db_table = " Student"

class Subject(Common_field):
    is_practical = models.BooleanField(default= False)
    total_marks = models.IntegerField(default= 100)
    student = models.ManyToManyField(Student)

    class Meta :
        db_table = " subject"




# C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project\second_app\models.py

# exec(open("C:\\Users\\Lenovo\\Desktop\\aniket\\b6\\Django\\first_project\\second_app\\models.py").read())
