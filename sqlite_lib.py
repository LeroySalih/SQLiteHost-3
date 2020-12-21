import sqlite3



def listTables(c):

  COMMAND = """
  
  SELECT 
    name
FROM 
    sqlite_master 
WHERE 
    type ='table' AND 
    name NOT LIKE 'sqlite_%';
  """

  c.execute(COMMAND)

  print("+" * 20)
  print('Found Tables:')
  print( c.fetchall())
  print("+" * 20)

#A Sub Proceedure to help execute SQL commands.
def SQL(command):

  conn = sqlite3.connect("test1.db")
  c = conn.cursor() 

  print("Executing Command:")
  print(command)
  c.execute(command)

  result = c.fetchall()

  if (len(result) > 0):
    
    #Print Header
    print("{0:>6}".format("Row"), end="")

    for col in c.description:
      print(" {0:>10}".format(col[0]), end="")

    print ()


    #Print Data
    for index, row in enumerate(result):
      #print row number
      print("{0:5}:".format(index + 1), end="")

      for fact in row:
        if isinstance(fact, str) and len(fact) > 10:
          f = fact[0:6] + "..."
        else: 
          f = fact 
        print (" {0:>10}".format(f), end="")

      print()


    print ("OK")
    print("=" * 40)
  else:
    print ("OK")
    print("=" * 40)

  conn.commit() 
  conn.close()