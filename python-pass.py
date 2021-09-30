#first we create an empty string to store the value in
#then we loop backwords through out string
#then update the variable if matched


def LongestPal(s) -> str:
    palindrome = ''

    for i in range(len(s)):

        for j in range(len(s), i, -1):

            if len(palindrome) >= j-i:
                break

            elif s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break

    print(palindrome) 
    
    
LongestPal("babad") 