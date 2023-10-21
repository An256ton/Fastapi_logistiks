import sqlalchemy 
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://login:passwordQ@server189.hosting.reg.ru/u2133606_default')

#функция исполнения запроса к бд
async def make_query(query):
    with engine.connect() as con:
        data=con.execute(query)
        result=[]
        for element in data:
            result.append(element)
    return  result          
