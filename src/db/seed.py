from db.connection import Connection

import os

def verify_tables():
    caminho = 'sql'
    ddl_arquivo = caminho + '/DDL.sql'
    dml_arquivo = caminho + '/DML.sql'
    
    
    if not os.path.exists(caminho): 
        os.makedirs(caminho)

    if not os.path.exists(ddl_arquivo): 
        open(ddl_arquivo, 'w')
        
    if not os.path.exists(dml_arquivo): 
        open(dml_arquivo, 'w')

    return ddl_arquivo, dml_arquivo

def create_tables():
    ddl_arquivo, dml_arquivo = verify_tables()
    
    conn_database = Connection()
    if conn_database is not None:
        cursor = conn_database.cursor
        try:
            execute_sql_script(cursor, ddl_arquivo)
            # print("Tabelas criadas com sucesso!")
            
             # Insere dados
            execute_sql_script(cursor, dml_arquivo)
            # print("Dados inseridos com sucesso!")
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
                #print(command)
                cursor.execute(command)
            except Exception as e:
                print(f"Erro ao executar comando: {e}")
                cursor.connection.rollback()
            else:
                cursor.connection.commit()

if __name__ == "__main__":
    create_tables()