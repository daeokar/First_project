 
#  >>>os.path.exists(r"C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project\first_project\settings.py")
# True
# >>>os.path.exists("C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project/first_project/settings.py"
# True

# > BASE_DIR = Path(r"C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project/first_project/settings.py").resolve().parent
# >>> BASE_DIR
# WindowsPath('C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project/first_project')
# >>>
# >>>
# >>> BASE_DIR = Path(r"C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project/first_project/settings.py").resolve().parent.parent
# >>> BASE_DIR
# WindowsPath('C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project')
# >>> BASE_DIR
# WindowsPath('C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project')
# >>> BASE_DIR = Path(r"C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project/first_project/settings.py").resolve().parent.parent.parent
# >>> base_dir
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'base_dir' is not defined
# >>> BASE_DIR
# WindowsPath('C:/Users/Lenovo/Desktop/aniket/b6/Django')
# >>>
# >>> BASE_DIR = Path(r"C:/Users/Lenovo/Desktop/aniket/b6/Django/first_project/first_project/settings.py").resolve().parent.parent.parent.parent
# >>> BASE_DIR
# WindowsPath('C:/Users/Lenovo/Desktop/aniket/b6')


# >>> os.path.dirname(r"C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project\first_project\settings.")
# 'C:\\Users\\Lenovo\\Desktop\\aniket\\b6\\Django\\first_project\\first_project'
# >>> os.path.os.path.dirname(r"C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project\first_project\settings.")
# 'C:\\Users\\Lenovo\\Desktop\\aniket\\b6\\Django\\first_project\\first_project'
# >>> os.path.dirname(os.path.dirname(r"C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project\first_project\settings."))
# 'C:\\Users\\Lenovo\\Desktop\\aniket\\b6\\Django\\first_project'
# >>> os.path.dirname(os.path.dirname(os.path.dirname(r"C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project\first_project\settings.")))
# 'C:\\Users\\Lenovo\\Desktop\\aniket\\b6\\Django'



# C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project>py manage.py migrate


# C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project>py manage.py runserver

# http://127.0.0.1:8000/admine

# C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project>py manage.py createsuperuser        
# Username (leave blank to use 'lenovo'): Aniket
# Email address: da@gmail.com
# Password: 
# Password (again):


# C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project>py manage.py help

# PS C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project> py manage.py changepassword createsuperuser_name


# [auth]
#     changepassword
#     createsuperuser

# [contenttypes]
#     remove_stale_contenttypes

# [django]
#     check
#     compilemessages
#     createcachetable
#     dbshell
#     diffsettings
#     dumpdata
#     flush
#     inspectdb
#     loaddata
#     makemessages
#     makemigrations
#     migrate
#     sendtestemail
#     shell
#     showmigrations
#     sqlflush
#     sqlmigrate
#     sqlsequencereset
#     squashmigrations
#     startapp
#     startproject
#     test
#     testserver

# [sessions]
#     clearsessions

# [staticfiles]
#     collectstatic
#     findstatic
#     runserver


# (base) C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project>python manage.py startapp second_app


# (base) C:\Users\Lenovo\Desktop\aniket\b6\Django\first_project>python manage.py sqlmigrate second_app 0001

# UPDATE `second_app`.`auth_user` SET `first_name` = 'Aniket', `last_name` = 'Dorokar' WHERE (`id` = '1');

# CREATE TABLE `second_app_student` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL, `age` integer NOT NULL, `marks` double precision NOT NULL);   



