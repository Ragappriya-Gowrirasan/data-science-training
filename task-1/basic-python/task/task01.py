# mail devide 
# concept: string method split
mail_name = input( 'Enter your mail name: ')
user_name = mail_name.split('@')
if len(user_name) ==2:
    part = user_name[0]
    print('Your mail name :' , part)
    part = user_name[1]
    print('your url address:' , part)
else:
    print('invalit mail address')


