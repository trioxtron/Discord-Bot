import discord
from discord.ext import commands
import sqlalchemy


class Mysqllib:
    
    def connect(self):
        url = 'mysql+pymysql://root:Triox0811@localhost/villains_bot?charset=utf8mb4'
        db = sqlalchemy.create_engine(url)
        return db



    def cursor(self):
        return self.connect()



    def insert(self, table, column : list, value : list):
        cursor  = self.cursor()
        columns = ""
        values  = ""
        
        for c in column:
            columns = columns + c
            if c != column[len(column) - 1]:
                columns = columns + ", "
                
        
        for v in value:
            values = values + '"' + str(v) + '"'
            if v != value[len(value) - 1]:
                values = values + ", "

        inserted = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(inserted)



    def update(self, table, column : list, value : list, condition : str, conditionvalue: str):
        cursor = self.cursor()
        columns = ""
        values  = ""

        for c in column:
            columns = columns + c
            if c != column[len(column) - 1]:
                columns = columns + ", "

        for v in value:
            values = values + '"' + str(v) + '"'
            if v != value[len(value) - 1]:
                values = values + ", "

        updated = f"UPDATE {table} SET {columns} WHERE {condition} = %s", (f"{values}", f"{conditionvalue}")
        cursor.execute(updated)



    def get(self, table, column : list, condition : str , form = 'normal'):
        cursor = self.cursor()
        columns = ""

        for c in column:
            columns = columns + c
            if c != column[len(column) - 1]:
                columns = columns + ", "
        
        if form == 'where':
            executed = f"SELECT {columns} FROM {table} WHERE {condition}"
        elif form == 'limit':
            executed = f"SELECT {columns} FROM {table} LIMIT {condition}"
        elif form == 'normal':
            executed = f"SELECT {columns} FROM {table}"
        else:
            executed = f"SELECT * FROM {table}"

        result = cursor.execute(executed)
        rows = result.fetchall()
        return(rows)



    def throw(self, table, condition: list):
        cursor = self.cursor()
        conditions = ""
        for c in condition:
            conditions = conditions + str(c)
            if c != condition[len(condition) - 1]:
                conditions = conditions + " AND "
        throwing = f"DELETE FROM {table} WHERE {conditions}"
        cursor.execute(throwing)



    def add(self, table, column : list , ctype : str):
        cursor = self.cursor()
        columns = ""

        for c in column:
            columns = columns + c
            if c != column[len(column) - 1]:
                columns = columns + ", "

        
        cursor.execute(f"ALTER TABLE {table} ADD {columns} {ctype}")



    def create(self, table, column : list):
        cursor = self.cursor()
        columns = ""

        for c in column:
            columns = columns + c
            if c != column[len(column) - 1]:
                columns = columns + ", "

        cursor.execute(f"CREATE TABLE {table} ({columns})")



    def checkrow(self, table, conval : str):
        cursor = self.cursor()

        executed = (f"SELECT 1 FROM {table} WHERE {conval}")

        result = cursor.execute(executed)
        rows = result.fetchall()
        return(rows)



exc = Mysqllib()

