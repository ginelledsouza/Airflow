import github.includes.postgresql as psql

def record_analysis():
    query = "select count(*) from feedbackdatabase;"
    value = psql.execute_query(psql.establish_connection(), query)[0][0]
    print("The number of records avaiable in the feedback database are {}".format(value))
    
def table_analysis():
    Tables = psql.existing_table(psql.establish_connection())
    print("The tables present in the database are")
    print(*Tables,sep=", ")
    
def extract_database():
    print ("Importing Table feedbackdatabase.....")
    columns = psql.get_columns_names(psql.establish_connection(),"feedbackdatabase")
    data = psql.postgresql_to_dataframe(psql.establish_connection(), "select * from feedbackdatabase", columns)
    print(data)