import argparse
import mysql.connector
def add_to_db(mycursor, list_of_lines, mydb):
	for i in range(len(list_of_lines)):
		sql = "INSERT INTO employee (id, name, dept, salary) VALUES (%s, %s, %s, %s)"
		arr = list_of_lines[i].split(', ')
		val = (int(arr[0]), arr[1], arr[2], int(arr[3]))
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-inp', type=argparse.FileType('r'))
    args = parser.parse_args()
    list_of_lines = args.inp.readlines()
    print(list_of_lines)
    
    
    mydb = mysql.connector.connect(
      host = "localhost",
      user = "ar.sehgal",
      passwd = "ar.sehgal",
      database = "testdb"
    )
    
    mycursor = mydb.cursor()
    add_to_db(mycursor, list_of_lines, mydb)

if __name__ == '__main__': 
    main() 
