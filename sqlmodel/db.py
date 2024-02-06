from sqlmodel import Field,SQLModel,create_engine,Session,select
from typing import Optional
from dotenv import load_dotenv
import  os
load_dotenv()
neon_link=os.getenv("Neon_db")


class Student(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
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

if __name__=="__main__":
    # getData()
    wherequery()




