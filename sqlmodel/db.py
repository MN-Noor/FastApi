from sqlmodel import Field,SQLModel,create_engine,Session,select,or_
from typing import Optional
from dotenv import load_dotenv
import  os
load_dotenv()
neon_link=os.getenv("Neon_db")


class Student(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str=Field(index=True)
    department:str
    section:str
    age:Optional[int]=Field(default=None)


engine=create_engine(neon_link,echo=True)
def create_db_tables():
    SQLModel.metadata.create_all(engine)

def getData():
    statement=select(Student)
    with Session(engine) as  session:
        result=session.exec(statement)
        student=result
        print(result.all())
def wherequery():
    statement=select(Student).where(Student.name=="Kainta")
    with Session(engine) as session:
        result=session.exec(statement)
        print(result.all())     
def add_Student():
    Student1=Student(name="Kainta",department="Faculty of Computing",section="BSITF20",age=22)
    Student2=Student(name="Ayesha",department="Faculty of Computing",section="BSITF20",age=22)

    with Session(engine)  as  session:
        session.add(Student1)
        session.add(Student2)
        session.commit()
def Andquery():
    # statement=select(Student).where(Student.age>21).where(Student.name=="wajia")
    statement=select(Student).where(Student.age<22,Student.department=="Faculty of Computing")
    with Session(engine) as session:
        result=session.exec(statement)
        print(result.all())
def ORquery():
    statement=select(Student).where(or_(Student.age>21,Student.department=="Faculty of Computing"))
    with Session(engine) as session:
        result=session.exec(statement)
        print(result.all())
def getQuery():
    with Session(engine)  as session:
        result=session.get(Student,3)
        print("result:",result)
def limitQuery():
    with Session(engine) as session:
        statement=select(Student).limit(3)
        result=session.exec(statement)
        print(result.all())
def offsetQuery():
    with Session(engine) as session:
            statement=select(Student).offset(3).limit(3)
            result=session.exec(statement)
            print(result.all())
def  updateQuery():
    statement=select(Student).where(Student.name=="Kainta")
    with  Session(engine)  as session:
        result=session.exec(statement).first()
        print(result)
        result.age=18
        session.add(result)
        session.commit()
        session.refresh(result)
        print("updated Student:",result)
def  deleteQuery():
    statement=select(Student).where(Student.name=="Ayesha")
    with Session(engine) as session:
        result=session.exec(statement)
        student=result.first()
        session.delete(student)
        session.commit()
        print("deleted student:",student)


    

        




if __name__=="__main__":
    deleteQuery()   
    # updateQuery()
    # offsetQuery()
    # limitQuery()
    # getData()
    # getQuery()
    # Andquery()
    # ORquery()




