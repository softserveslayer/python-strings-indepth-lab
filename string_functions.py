    
import re
# def say_hello(name):
#     # takes in a name and returns the string "Hi my name is " plus the name
#     # use whichever form of interpolation is most appropriate
#     pass

def say_hello(name):
    return "Hi my name is " + name

def say_hello(name):
    return "Hi my name is {n}".format(n=name)

def replace_given_substring(str_to_replace, str_to_insert, string):
    # this function takes three parameters --
    # the first is the substring we would like to replace.
    # the second substring is what we would like to use inplace of the first
    # the third is the actual string which we want to operate on
    # the function should return the new string
    pass


def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace, str_to_insert)


def remove_duplicate_punctuation(string):
    # should remove all duplicate punctuation marks in a given string
    # i.e. "Hi!!!!!!" should be reformatted to "Hi!"
    # i.e. "Hello..... My name is Terrance!! How are you???" -> "Hello. My name is Terrance! How are you?"
    return re.sub(r"(\W)\1*", r'\1', string)



def validate_email_format(email):
    split_email = email.split("@")
    if re.match("^[a-zA-Z0-9_]*$", split_email[0]) and re.match("^[a-zA-Z0-9_\.]*$", split_email[1]):
        return "good email"
    else:
        return "bad email, try again but RIGHT this time"

    # should make sure there are no special characters (i.e. *,~,#,$,%,&,(,),`,",',:,;,/,>,<)
    # make sure the email contains an @ symbol and a .com
    # return True if format passes tests, return False otherwise    


def anonymize_credit_card_number(credit_card_number):
    shortened_string = credit_card_number[:-4]
    for digit in shortened_string:
        if digit != "-":
            shortened_string = shortened_string.replace(digit, "X")
    return shortened_string + credit_card_number[-4:]  

    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234