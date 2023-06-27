class Config:
    # 设置连接数据库的URL
    user = 'root'
    password = 'Bigmouse213'
    database = 'resumeidentification'
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@123.60.9.217/%s' % (user, password, database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    # SQLALCHEMY_ECHO = True

