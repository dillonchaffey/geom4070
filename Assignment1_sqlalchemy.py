from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:SECRETPASSWORD@127.0.0.1:5432"

db = create_engine(db_string)  
base = declarative_base()

class Student(base):  
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)
    address = Column(String)
    city = Column(String)
    province = Column(String)
    program = Column(String)
    
class Course(base):  
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    program = Column(String)
    instructor = Column(String)
    
class Marks(base):  
    __tablename__ = 'marks'

    student_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=True)
    grade = Column(Float)
    
class Program(base):  
    __tablename__ = 'program'

    program_id = Column(String, primary_key=True)
    program_name = Column(String)
    lead_faculty = Column(String)  


Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)
