from sys import exc_info
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

# 编码格式在数据库 URI 中就要设置好
# 必须写成utf8，写成utf-8无效
engine = create_engine("mysql+pymysql://%s:%s@%s:%s/test?charset=utf8"
                       % ('root', 'mwzfy74701', 'localhost', '3306'),
                       echo=True)


def date_check_and_convert(column_data):
    """
    ◆ 日期检验和转换函数
        用于检验用户所指定的日期列是否合法——取值是否规范，且是否为 SQLAlchemy 能够识别的 Python 日期对象（datetime.date）。
        本函数会把日期字符串（形如“2016-12-19”）转换为 SQLAlchemy 能够识别的 Python 日期对象（datetime.date）。
        SQLAlchemy 的日期类型只接受这一格式，所以若要使用则必须转换。
    :param column_data: 用户所输入的日期列数据。可能是日期字符串，也有可能是已经部署好的日期对象。
    :return: 无返回值，但会在终端中报错。
    """
    # 对日期的特别处理
    from datetime import datetime
    try:
        if type(column_data) == str:
            if column_data == '' or column_data == None:
                pass
            else:
                return datetime.strptime(column_data, "%Y-%m-%d").date()
        elif type(column_data) == datetime:
            pass
    except ValueError:
        print("Found an exception of err date format...")
    except:
        print("Unexpected error occurred: ", exc_info()[0])
    # else:
    #    raise ValueError("Date format or value error. Preferred format is YYYY-mm-dd. ")


def create_all_tables():
    """
    ◆ 创建所有表
        用于服务端 MySQL 的部署。
    :return:
    """
    Base.metadata.create_all(engine)