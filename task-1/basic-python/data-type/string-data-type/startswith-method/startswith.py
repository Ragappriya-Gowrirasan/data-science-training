# method returns if a string start 
text = "language is tamil"
start = text.startswith('tamil')
print(start) # false

#example 1
text1 = "python programming is very easy"
text2 = text1.startswith('easy',24)
print(text2) # False


#example 2
text3 = "Success is not final; failure is not fatal: It is the courage to continue that counts"
text4 = text3.startswith(('success is not'),1)
print(text4)


