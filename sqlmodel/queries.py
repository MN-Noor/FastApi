from sqlmodel import SQLModel,Session
from dotenv import load_dotenv
import os
load_dotenv()
neon_link=os.getenv("Neon_db")

with(Session)  as session:
    statement=select(student).where
