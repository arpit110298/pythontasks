
# TODO: File naming should be better

# TODO: Start using shebang statments
# https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take
import re 

def main():
    # TODO: use getpass instead of input(), it does not echo the typed password
    # https://docs.python.org/2/library/getpass.html

    passwd = input("enter password")
    regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,}$"
    pattern = re.compile(regexp)                  
    if re.search(pattern, passwd) : 
        print("Accepted") 
    else: 
        # TODO: Why not accepted. print the reason. Would help the user to enter a valid password on next try
        print("Not Accepted") 
  

if __name__ == '__main__': 
    main() 
