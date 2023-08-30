# contact book page

### start the contact page ##

phone_book = {}
while True:
    print('1.add contact')
    print('2.view contact')
    print('3.search contact')
    print('4.delete contact')
    print('5.exit')

    contact =(input('enter the choice number of the contact: '))

    if contact =='1':
        name = input('type the contact name: ')
        number = input('enter the contact number: ')
        mail = input('type the mail address: ')
        phone_book = {'name':name , 'number':number , 'mail address':mail}
        print('The contact is successfuly saved')
    elif contact =='2':
        print('contact details: ',phone_book)
    elif contact =='3':
        search = input('enter the contact name: ')
        for search_name in (phone_book):
            search == phone_book
            print(search_name)
        #search_name = search.check(phone_book)
        #search == search_name
       # print(search)
    elif contact == '4':
        delete_contact = input('enter the delete contact name: ')
        delete_contact = phone_book.clear()
        print('this contact is remove')
    elif contact == '5':
        print('exit contact')
    else:
        print('contact is exit')

