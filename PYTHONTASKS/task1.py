import re 

def main():
    passwd = input("enter password")
    regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,}$"
    pattern = re.compile(regexp)                  
    if re.search(pattern, passwd) : 
        print("Accepted") 
    else: 
        print("Not Accepted") 
  

if __name__ == '__main__': 
    main() 
