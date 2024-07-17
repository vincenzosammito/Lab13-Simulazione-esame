from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def get_shape(anno):
        conn = DBConnect.get_connection()
        result = []
        cur = conn.cursor(dictionary=True)
        query = """select DISTINCT (s.shape) as forma
                    from sighting s 
                    where YEAR (s.`datetime`) = %s
 """
        cur.execute(query, [anno])
        for row in cur:
            result.append(row["forma"])
        cur.close()
        conn.close()
        return result
    @staticmethod
    def stati():
        conn = DBConnect.get_connection()
        result = []
        cur = conn.cursor(dictionary=True)
        query = """select DISTINCT (s.id) as stato
from state s 
        """
        cur.execute(query)
        for row in cur:
            result.append(row["stato"])
        cur.close()
        conn.close()
        return result

    @staticmethod
    def neighborns(stato):
        conn = DBConnect.get_connection()
        result = []
        cur = conn.cursor(dictionary=True)
        query = """select state2 as stato
from neighbor n 
where n.state1 = %s
            """
        cur.execute(query, [stato])
        for row in cur:
            result.append(row["stato"])
        cur.close()
        conn.close()
        return result

    @staticmethod
    def peso_stati(stato, forma, anno ):
        conn = DBConnect.get_connection()
        result = []
        cur = conn.cursor(dictionary=True)
        query = """select COUNT(s.id) as count
from sighting s 
where s.state = %s and s.shape = %s and YEAR(s.datetime) = %s """
        cur.execute(query, [stato, forma, anno,])
        for row in cur:
            result.append(int(row["count"]))
        cur.close()
        conn.close()
        return result