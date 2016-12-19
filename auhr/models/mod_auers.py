from auhr.models.common import *


class AUers(Base):
    """
    ■ 成员信息表的数据结构
    """
    __tablename__ = 'AUers'
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    Name = Column(String(64), nullable=False)
    Gender = Column(String(64))
    Mobile = Column(String(64))
    QQ = Column(String(64))
    Grade = Column(String(64))
    Faculty = Column(String(64))
    Class = Column(String(64))
    DormBuild = Column(String(64))
    Department = Column(String(64))
    Group = Column(String(64))
    Occupation = Column(String(64))
    AUID = Column(String(64))
    Birthday = Column(Date)
    JoinTime = Column(Date)

    def __repr__(self):
        return "<AUer %s>" % self.Name


def insert(**data):
    """
    ■ 插入新的记录
    :param data: 一连串的字典条目，为你需要插入的成员信息。允许留空。
    :return: 若操作成功，则返回 True；否则返回 False，并在终端中报错。
    """
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    data.setdefault("name", "")
    data.setdefault("gender", "")
    data.setdefault("mobile", "")
    data.setdefault("qq", "")
    data.setdefault("grade", "")
    data.setdefault("faculty", "")
    data.setdefault("class_", "")
    data.setdefault("dormbuild", "")
    data.setdefault("department", "")
    data.setdefault("group", "")
    data.setdefault("occupation", "")
    data.setdefault("auid", "")
    data.setdefault("birthday", None)
    data.setdefault("jointime", None)

    # 对日期的特别处理
    data['birthday'] = date_check_and_convert(data['birthday'])
    data['jointime'] = date_check_and_convert(data['jointime'])

    # 生成新记录
    rec = AUers(Name=data['name'], Gender=data['gender'], Mobile=data['mobile'],
                QQ=data['qq'], Grade=data['grade'],
                Faculty=data['faculty'], Class=data['class_'], DormBuild=data['dormbuild'],
                Department=data['department'], Group=data['group'], Occupation=data['occupation'],
                AUID=data['auid'], Birthday=data['birthday'], JoinTime=data['jointime'])

    session.add(rec)

    try:
        session.commit()
    except:
        print("Unexpected error occured: ", exc_info()[0])
        session.rollback()
        return False
    else:
        return True


def query(keyword):
    """
    ■ 根据关键字查询记录
    :param keyword: 用于查询的关键字。函数会逐条记录逐列来进行匹配。
    :return: 查询所得的结果集，是一个盛放数据结构对象的 list。
    """
    from sqlalchemy.sql.elements import or_

    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    key_for_sql_query = "%"+keyword+"%"
    query_boundary = or_(AUers.Name.like(key_for_sql_query),
                        AUers.Gender.like(key_for_sql_query),
                        AUers.Mobile.like(key_for_sql_query),
                        AUers.QQ.like(key_for_sql_query),
                        AUers.Grade.like(key_for_sql_query),
                        AUers.Faculty.like(key_for_sql_query),
                        AUers.Class.like(key_for_sql_query),
                        AUers.DormBuild.like(key_for_sql_query),
                        AUers.Department.like(key_for_sql_query),
                        AUers.Group.like(key_for_sql_query),
                        AUers.Occupation.like(key_for_sql_query),
                        AUers.AUID.like(key_for_sql_query),
                        AUers.Birthday.like(key_for_sql_query),
                        AUers.JoinTime.like(key_for_sql_query))
    results = session.query(AUers).filter(query_boundary).all()

    return results


def modify(unique_id, **data):
    """
    ■ 根据唯一索引检索并修改记录
    :param unique_id: 要修改之记录的唯一索引。只有唯一索引才是准确区分条目的依据。
    :param data: 一连串的字典条目，指定你要修改的条目及其内容。部分条目取值可忽略，即允许不改。
    :return: 若操作成功，则返回 True；否则返回 False，并在终端中报错。
    """
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    # 先查询
    key_for_sql_query = int(unique_id)
    result = session.query(AUers).filter(AUers.id == key_for_sql_query).first()

    # 指定参数默认值
    data.setdefault("name", result.Name)
    data.setdefault("gender", result.Gender)
    data.setdefault("mobile", result.Mobile)
    data.setdefault("qq", result.QQ)
    data.setdefault("grade", result.Grade)
    data.setdefault("faculty", result.Faculty)
    data.setdefault("class_", result.Class)
    data.setdefault("dormbuild", result.DormBuild)
    data.setdefault("department", result.Department)
    data.setdefault("group", result.Group)
    data.setdefault("occupation", result.Occupation)
    data.setdefault("auid", result.AUID)
    data.setdefault("birthday", result.Birthday)
    data.setdefault("jointime", result.JoinTime)

    # 对日期的特别处理
    data['birthday'] = date_check_and_convert(data['birthday'])
    data['jointime'] = date_check_and_convert(data['jointime'])

    # 后修改
    result.Name = data['name']
    result.Gender = data['gender']
    result.Mobile = data['mobile']
    result.QQ = data['qq']
    result.Grade = data['grade']
    result.Faculty = data['faculty']
    result.Class = data['class_']
    result.DormBuild = data['dormbuild']
    result.Department = data['department']
    result.Group = data['group']
    result.Occupation = data['occupation']
    result.AUID = data['auid']
    result.Birthday = data['birthday']
    result.JoinTime = data['jointime']

    # 最后提交
    try:
        session.commit()
    except:
        print("Unexpected error occured: ", exc_info()[0])
        session.rollback()
        return False
    else:
        return True


def remove(unique_id):
    """
    ■ 根据唯一索引移除记录
    :param unique_id: 要修改之记录的唯一索引。只有唯一索引才是准确区分条目的依据。
    :return: 若操作成功，则返回 True；否则返回 False，并在终端中报错。
    """
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    # 先查询
    key_for_sql_query = int(unique_id)
    result = session.query(AUers).filter(AUers.id == key_for_sql_query).first()

    # 检查是否存在
    if result.__repr__().find("AUer") < 0:
        print("ERR: The item you want to remove is not exist.")
        return False

    # 后移除
    session.delete(result)

    # 最后提交
    try:
        session.commit()
    except:
        print("Unexpected error occurred: ", exc_info()[0])
        session.rollback()
        return False
    else:
        return True








    

