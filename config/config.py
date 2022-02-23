class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'    #Agregar el nombre o dirección de tu HOST de base de datos
    MYSQL_USER = 'root'         #Agregar tu nombre de usuario en MySQL
    MYSQL_PASSWORD = 'rootRafael'   #Agregar tu contraseña de usuario en MySQL
    MYSQL_DB = 'sepomex'        #Agrega el nombre la base de datos
    
config = {
    'development': DevelopmentConfig
}