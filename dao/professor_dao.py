from dao.base_dao import BaseDAO

class ProfessorDAO(BaseDAO):

    sql_select = "SELECT id, nome, disciplina FROM professor"
