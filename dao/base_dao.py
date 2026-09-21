from dao.db_config import get_connection


class BaseDAO:


    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sql_select)
        lista = cursor.fetchall()
        conn.close()
        return lista