from database.conexao import conectar
from models.livro import Livro
from models.revista import Revista


class BancoDeDados:

    # Cria as tabelas do sistema
    def preparar_banco(self):

        sql = """
        CREATE TABLE IF NOT EXISTS tabela_itens(

            isbn VARCHAR(50) PRIMARY KEY,
            titulo VARCHAR(255),
            tipo VARCHAR(30),
            autor VARCHAR(255),
            edicao INT,
            disponivel BOOLEAN DEFAULT TRUE

        );

        CREATE TABLE IF NOT EXISTS tabela_emprestimos(

            id SERIAL PRIMARY KEY,
            id_usuario VARCHAR(50),
            isbn_item VARCHAR(50)
            REFERENCES tabela_itens(isbn)

        );
        """

        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

            conn.commit()

    # Salva um livro ou revista
    def salvar_item(self, item):

        autor = item.autor if isinstance(item, Livro) else None
        edicao = item.edicao if isinstance(item, Revista) else None

        tipo = "Livro" if isinstance(item, Livro) else "Revista"

        sql = """
        INSERT INTO tabela_itens
        (isbn,titulo,tipo,autor,edicao,disponivel)

        VALUES(%s,%s,%s,%s,%s,%s)

        ON CONFLICT(isbn)
        DO UPDATE SET

        titulo=EXCLUDED.titulo,
        tipo=EXCLUDED.tipo,
        autor=EXCLUDED.autor,
        edicao=EXCLUDED.edicao,
        disponivel=EXCLUDED.disponivel;
        """

        with conectar() as conn:
            with conn.cursor() as cur:

                cur.execute(sql, (
                    item.isbn,
                    item.titulo,
                    tipo,
                    autor,
                    edicao,
                    item._disponivel
                ))

            conn.commit()

    # Lista todos os itens
    def listar_itens(self):

        with conectar() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    SELECT isbn, titulo, tipo, autor, edicao, disponivel
                    FROM tabela_itens
                    ORDER BY titulo;
                """)

                return cur.fetchall()

    # Busca um item pelo ISBN
    def buscar_item(self, isbn):

        with conectar() as conn:
            with conn.cursor() as cur:

                cur.execute("""

                    SELECT *
                    FROM tabela_itens
                    WHERE isbn=%s;

                """, (isbn,))

                return cur.fetchone()

    # Atualiza o título do item
    def atualizar_item(self, isbn, novo_titulo):

        with conectar() as conn:
            with conn.cursor() as cur:

                cur.execute("""

                    UPDATE tabela_itens
                    SET titulo=%s
                    WHERE isbn=%s;

                """, (novo_titulo, isbn))

            conn.commit()

    # Exclui um item
    def excluir_item(self, isbn):

        with conectar() as conn:
            with conn.cursor() as cur:

                cur.execute("""

                    DELETE FROM tabela_itens
                    WHERE isbn=%s;

                """, (isbn,))

            conn.commit()

    # Registra um empréstimo
    def registrar_emprestimo_no_banco(self, id_usuario, isbn):

        with conectar() as conn:
            with conn.cursor() as cur:

                cur.execute("""

                    INSERT INTO tabela_emprestimos
                    (id_usuario,isbn_item)
                    VALUES(%s,%s);

                """, (id_usuario, isbn))

                cur.execute("""

                    UPDATE tabela_itens
                    SET disponivel=FALSE
                    WHERE isbn=%s;

                """, (isbn,))

            conn.commit()
