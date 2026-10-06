from dao.base_dao import BaseDAO

class CursoDAO(BaseDAO):

    sql_select = "SELECT id, nome_curso, duracao FROM curso ORDER BY id ASC"