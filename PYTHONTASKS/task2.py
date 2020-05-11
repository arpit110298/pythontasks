import argparse
import mysql.connector
def add_to_db(mycursor, list_of_lines, mydb):
        # TODO: Why not use --> for line in list_of_lines
	for i in range(len(list_of_lines)):
		sql = "INSERT INTO employee (id, name, dept, salary) VALUES (%s, %s, %s, %s)"
		arr = list_of_lines[i].split(', ')
		val = (int(arr[0]), arr[1], arr[2], int(arr[3]))
                # TODO: Does the mycursor prints the query which is being executed ? If not, then print the query being executed
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")


def main():
    parser = argparse.ArgumentParser()
    # TODO: What if no file is passed ?
    parser.add_argument('-inp', type=argparse.FileType('r'))
    args = parser.parse_args()
    list_of_lines = args.inp.readlines()
    print(list_of_lines)
    
    
    # TODO:  Would've been better to create separate function for connection
    mydb = mysql.connector.connect(
      host = "localhost",
      user = "ar.sehgal",
      passwd = "ar.sehgal",
      database = "testdb"
    )
    
    mycursor = mydb.cursor()
    add_to_db(mycursor, list_of_lines, mydb)
    # TODO: Forgot to close the connection
    # TODO: Read about 'with' statement and see how it can be used here

if __name__ == '__main__': 
    main() 
