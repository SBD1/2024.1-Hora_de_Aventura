from db.connection import Conection

def create_tables(script_path='../sql/DDL.sql'):
    conn = Conection()
    if conn.conn is not None:
        cursor = conn.cursor
        try:
            execute_sql_script(cursor, script_path)
            print("Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")
        finally:
            cursor.close()
    else:
        print("Falha ao conectar ao banco de dados.")
    

def execute_sql_script(cursor, script_path):
    with open(script_path, 'r') as file:
        sql_script = file.read()
        
    # Divide o script em comandos individuais
    sql_commands = sql_script.split(';')

    for command in sql_commands:
        # Ignora comandos vazios
        if command.strip():
            try:
                cursor.execute(command)
            except Exception as e:
                print(f"Erro ao executar comando: {e}")
                cursor.connection.rollback()
            else:
                cursor.connection.commit()

if __name__ == "__main__":
    create_tables()