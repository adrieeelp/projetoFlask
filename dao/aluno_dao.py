from dao.base_dao import BaseDAO

class AlunoDAO(BaseDAO):

    sql_select = "SELECT id, nome, idade, cidade FROM aluno ORDER BY id ASC"