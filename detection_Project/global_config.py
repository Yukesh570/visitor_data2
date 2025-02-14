import os 
from dotenv import load_dotenv

load_dotenv()



# DATABASE
POSTGRES_HOST = os.getenv("POSTGRES_HOST")# type: ignore
POSTGRES_PORT = os.getenv("POSTGRES_PORT")# type: ignore
POSTGRES_DB = os.getenv("POSTGRES_DB")# type: ignore
POSTGRES_USER = os.getenv("POSTGRES_USER")# type: ignore
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")# type: ignore



SECRET_KEY = 'django-insecure-duk^3v^(ys(t+t9$iupk1-)p$_xwt7lg#ug01#&5&%ozy%$n65'
