from database.DB_connect import DBConnect
from model.giocatore import Giocatore


class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getAllNodes(anno, salario):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select s.playerID, p.nameFirst as name, p.nameLast as surname, s.salary as salary
            from salaries s, people p 
            where s.`year` = %s  and s.salary > %s and p.playerID = s.playerID 
        """
        cursor.execute(query, (anno, salario,))
        result = []
        for row in cursor:
            result.append(Giocatore(**row))
        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getEdge(u, v, anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select a1.playerID as p1, a2.playerID as p2
            from appearances a1, appearances a2
            where a1.playerID = %s and a2.playerID = %s and a1.`year` = %s and a1.`year` = a2.`year` and a1.teamCode = a2.teamCode
                """
        try:
            cursor.execute(query, (u, v, anno,))
        except Exception as e:
            print(e)
            cursor.close()
            conn.close()
            return []
        result = []
        for row in cursor:
            result.append((row["p1"], row["p2"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeams(u, anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        select teamCode 
        from appearances a 
        where a.playerID = %s and `year` = %s 
        """
        cursor.execute(query, (u, anno, ))
        result = []
        for row in cursor:
            result.append(row["teamCode"])
        cursor.close()
        conn.close()
        return result
