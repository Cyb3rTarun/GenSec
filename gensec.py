#------------------------------------------------------------#
# string.ascii_lowercase = abcdefghijklmnopqrstuvwxyz        #   
# string.ascii_uppercase = ABCDEFGHIJKLMNOPQRSTUVWXYZ        #
# string.digits          = 0123456789                        #
# string.punctuation     = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  #
#------------------------------------------------------------#
#-------------------------------------------------------BEGINING OF THE CODE--------------------------------------------------------
import string 
import random
from pyfiglet import figlet_format

#for printing the banner.
print('-'*90)
ascii_banner = figlet_format("TARUN", font="isometric1")
print(ascii_banner)
print("-"*37+"PASSWORD STRENGTH"+"-"*36)
#end of printing the banner code.


#function for generating the password.
def generate_password(*lengths):
    """generating the password based on the user input character length."""

    #initializing the password list.
    password = []
    # for loop for appending the uppercase letters.
    for i in range(lengths[0]):
        password.append(random.choice(lengths[4]))
    # for loop for adding the lowercase letters.
    for i in range(lengths[1]):
        password.append(random.choice(lengths[5]))
    # for loop for adding the digits.
    for i in range(lengths[2]):
        password.append(random.choice(lengths[6]))
    # frr loop for adding the special characters(punctuations).
    for i in range(lengths[3]):
        password.append(random.choice(lengths[7]))
    # shuffling the password to generate a high secure password.
    random.shuffle(password)
    # returning the password as a string.
    return ''.join(password)


#function for counting the consecutive uppercase letters.
def consecutive_uppercase(password):
    """count for uppercase consecutive letters."""

    # initializing the count value to 0.
    count = 0
    # loop for finding the count
    for i in range(len(password)-1):
        # condition for checking the next letters as uppercase letter.
        if (password[i].isupper() == password[i+1].isupper() == True):
            count += 1
    #return for number of consecutive upppercase letters.
    return count


#function for counting the consecutive lowercase letters.
def consecutive_lowercase(password):
    """count for lowercase consecutive letters."""

    # initializing the count value to 0.
    count = 0
    # loop for finding the count
    for i in range(len(password)-1):
        # condition for checking the next letters as lowercase letter.
        if (password[i].islower() == password[i+1].islower() == True):
            count += 1
    #return for number of consecutive lowercase letters.
    return count


#function for counting the consecutive numbers.
def consecutive_numbers(password):
    """count for consecutive numbers."""
    # initializing the count value to 0.
    count = 0
    # loop for finding the count
    for i in range(len(password)-1):
        # condition for checking the next letters as number.
        if (password[i].isdigit() == password[i+1].isdigit() == True):
            count += 1
    #return for count of consecutive numbers.
    return count


# function for if all the letters in password are only letters
def only_letters(password):
    """length of password if password is completely alphabets."""
    #initializing the lenght to 0. 
    letter_length = 0
    # condition for checking the password is alphabets or not.
    if (password.isalpha()):
        letter_length = len(password)
    # brings the lenght of the password.
    return letter_length


# function for if all the letters in password are only letters
def only_numbers(password):
    """length of password if password is completely alphabets."""
    #initializing the lenght to 0.
    number_length = 0
    # condition for checking the password is alphabets or not.
    if(password.isdigit()):
        number_length = len(password)
    # brings the lenght of the password.
    return number_length


# fucntion for finding the pros of generated password.
def strength_addition(*add):
    """calculating the required strengths of generated password."""

    #passwordlength.
    passwordlength = len(add[0])
    #no of uppercase letters.
    no_uppercase = add[1]
    #no of lowercase letters.
    no_lowercase = add[2]
    #no of digits letters.
    no_digits = add[3]
    #no of special character letters.
    no_specialchar = add[4]
    #return the sum of the strengths.
    return (passwordlength + no_uppercase + no_lowercase + no_digits + no_specialchar)

def strength_subtraction(*sub):
    """calculating the required strengths of generated password."""

    #no of only letters.
    only_letters = sub[0]
    #no of only numbers.
    only_numbers = sub[1]
    #no of consecutive uppercase letters.
    consec_upper = sub[2]
    #no of consecutive lowercase letters.
    consec_lower = sub[3]
    #no of consecutive numbers.
    consec_number = sub[4]
    # return the sum of weakness of password.
    return (only_letters + only_numbers + consec_lower + consec_upper + consec_number)



#function for showing how high the password is secure.
def secure(s_value):
    """for displaying the security of the password."""

    # condition is strength value is less than or equal to 20.
    if (s_value <= 20):
        print("---> The Password is not secure enought to use. Can be easily bruteforced. [VERY WEAK]. ")
    # condition is strength value is greater than 20 and less than or equal to 25.
    elif (s_value > 20 and s_value <= 25):
        print("---> A bit risky to use this Password [WEAK]. ")
    # condition is strength value is greater than 25 and less than or equal to 45.
    elif(s_value >25 and s_value <= 45):
        print("---> The password strength is good. You can use it for less important sites. [MODERATE]. ")
    # condition is strength value is more than 45.
    else:
        print("---> The Password is Very High Secured. Can't be easily Bruteforced. [VERY GOOD]. ")


# Main function of the file.
def main():
    """Main function. """

    print('-'*90)
    # uppercase length. 
    uc_length = int(input("[*] Uppercase Length  : "))
    # lowercase length. 
    lc_length = int(input("[*] Lowercase Length  : "))
    # number length. 
    n_length = int(input("[*] Numbers Length    : "))
    # specialcharacter length. 
    sc_length = int(input("[*] Specialcase Length: "))
    print('-'*90)

    # assinging the uppercase alphabets from the string module.
    uc_letters = string.ascii_uppercase
    # assinging the lowercase alphabets from the string module.
    lc_letters = string.ascii_lowercase
    # assinging the numbers from the string module.
    d = string.digits
    # assinging the special characters from the string module.
    sc = string.punctuation

    # instance for the generated password to password variable.
    password = generate_password(uc_length, lc_length, n_length, sc_length, uc_letters, lc_letters, d, sc )
    # instance for counting for only letters.
    o_letter = only_letters(password)
    # instance for counting for only numbers.
    o_number = only_numbers(password)
    # instance for counting for uppercase letters.
    c_upper = consecutive_uppercase(password)
    # instance for counting for lowercase letters.
    c_lower = consecutive_lowercase(password)
    # instance for counting for only digits.
    c_digits = consecutive_numbers(password)
    # Generated Password output on the monitor.
    print("---> GENERATE PASSWORD: ", password)
    strength_value = strength_addition(password,uc_length, lc_length, n_length, sc_length) - strength_subtraction(o_letter, o_number, c_upper, c_lower, c_digits)
    print('-'*90)
    #output for password strength. 
    secure(strength_value)
    print('-'*90)

main()

#--------------------------------------END OF THE CODE FOR GENERATING PASSWORD.---------------------------------------------
