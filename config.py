DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/mysqldb'
# зміниш root - на свого користувача, admin - на свій пароль, mysqldb - на назву своєї бази даних
SECRET_KEY = 'Stuff'
# localhost:5000/stuff/1 - для get запиту, для post - localhost:5000/stuff
# Приклад json для postppp
# {
# 	"id" : 2,
# 	"name" : "Name",
# 	"price" : 3,
# 	"producer" : "Producer",
# 	"material" : "Material",
# 	"weight" : 5,
# 	"stuff_type" : "Type"
# }
# У terminal у самому pycharm у проекті де буде ця лаба пропиши
# pip install flask_sqlalchemy
# pip install flask_marshmallow
# pip install mysql-connector
