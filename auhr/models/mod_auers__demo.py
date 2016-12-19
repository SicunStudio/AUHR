from auhr.models.mod_auers import *


def demo_insert():
    insert(name=input("Name: "),
           gender=input("Gender: "),
           mobile=input("Mobile: "),
           QQ=input("QQ: "),
           grade=input("Grade: "),
           faculty=input("Faculty: "),
           class_=input("Class: "),
           dormbuild=input("Dorm Build: "),
           department=input("Department: "),
           group=input("Group: "),
           occupation=input("Occupation:　"),
           auid=input("AUID: "),
           birthday=input("Birthday: "),
           jointime=input("Join Time: ")
           )


def demo_modify_all_columns():
    a = input("Input the ID of the item you want to modify: ")
    modify(unique_id=int(a),
           name=input("Name: "),
           gender=input("Gender: "),
           mobile=input("Mobile: "),
           QQ=input("QQ: "),
           grade=input("Grade: "),
           faculty=input("Faculty: "),
           class_=input("Class: "),
           dormbuild=input("Dorm Build: "),
           department=input("Department: "),
           group=input("Group: "),
           occupation=input("Occupation:　"),
           auid=input("AUID: "),
           birthday=input("Birthday: "),
           jointime=input("Join Time: ")
           )


def demo_query():
    a = input("Input a keyword: ")
    print(query(a))


def demo_remove():
    a = input("Input the ID of the item you want to remove: ")
    print(remove(unique_id=int(a)))

if __name__ == "__main__":
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    demo_insert()
    # demo_query()
    # demo_remove()



