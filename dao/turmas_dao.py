from dao.base_dao import BaseDAO

class TurmaDAO(BaseDAO):

    sql_select = """select turma.id,turma.semestre,curso.nome_curso,professor.nome,professor.disciplina from turma
                    join curso on curso.id=turma.curso_id
                    join professor on professor.id=turma.professor_id
                    ORDER BY turma.id ASC"""
