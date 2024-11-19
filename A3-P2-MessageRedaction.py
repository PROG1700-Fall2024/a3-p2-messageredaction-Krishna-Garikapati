#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:  W0502117 
#Student Name: Krishna Priyanka, Garikapati 

def Replace():
    phrase=""
    letter=""
    #i want run the loop and ask for inputs until phrase = quit, the exit loop.
    while True:

        #lets give input values
        phrase=input("Type a phrase (or type quit to exit program):")
        if phrase.lower()=="quit":
            break
        letter=input("Type a Comma-separated list of letters to redact:")

        #I want values given separated by comma as different values. So using split function.
        letterstoRedact=letter.split(",")
        #print(letterstoRedact)

        #now replace each value from input received in the phrase input received.
        for value in letterstoRedact:
            phrase=phrase.replace(value.lower(),'_')
            phrase=phrase.replace(value.upper(),'_')
            #to count number of letters replaced or redacted
            count=phrase.count('_')
        print("Number of letters redacted: {0}".format(count))
        print("Redacted phase: {0}".format(phrase))
        





def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    Replace()
    
    # YOUR CODE ENDS HERE

main()
