# phone contact book
# name,number,mail
#user_input

# add_contact
contact_list= {}
def add_contact(contact):
    user_name = input('enter name: ')
    user_phone_num =int(input('enter mobile number: '))
    user_mail = input('enter the mail')
    contact_list['name']=
    contact.append(contact_list)
    print('The contact added successfully !!!! ')


# view_contact
def view_contact(contact):
    for contact_list in contact:
        print(contact)
    else:
        print('The contact is empty')


# search_contact
def sreach_contact(contact):
    search_name = input('enter search the name: ')



# loop statement
while True:
    print('1. add-contact')
    print('2. view-contact')
    print('3. search-contact')
    print('4. delete-contact')
    print('5. quit')
    choose_contacts = int(input('enter your choose number: '))

    if choose_contacts == 1:
        add_contact(contact)
    elif choose_contacts ==2:
        view_contact(contact)
    elif choose_contacts ==3:
        search_contact(contact)
    elif choose_contacts ==4:
        deleted_contact(contact)
    elif choose_contacts ==5:
        break
    print('exting the contact')







