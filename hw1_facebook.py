class Facebook:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email

    def printAll(self):
        print('first_name: ' + self.first_name)
        print('last_name: ' + self.last_name)
        print('mobile: ' + self.mobile)
        print('email: ' + self.email)


#------------------------------------------------------------------



def create():
    global face_dict
    element = Facebook(input("What's your first name?"), input("What's your last name?"),
                       input("What's your mobile phone number?"), input("What's your email address?"))
    face_dict[element] = {'first_name': element.first_name, 'last_name': element.last_name, 'mobile': element.mobile, 'email': element.email}


def read_all(face_dict):
    for e in face_dict.keys():
        e.printAll()
        print('None\n')

def read_by_condition(face_dict):
    keyword = input('keyword> ')
    items_having_keyword = []
    for k, v in face_dict.items():
        # keyword 부분일치인 경우
        if keyword in v['first_name'] or keyword in v['last_name'] or keyword in v['mobile'] or keyword in v['email']:
            items_having_keyword.append(k)
        #
        # # keyword 완전일치인 경우
        # if v['first_name'] == keyword or v['last_name'] == keyword or v['mobile'] == keyword or v['email'] == keyword:
        #     keyword_y_items_idx.append(k)
    #
    print('There is(are) %s item(s).' % len(items_having_keyword))
    for i in items_having_keyword:
        i.printAll()
        print('None\n')


face_dict = {}

while True: #무한 루프
    select_menu = input("Choose the menu you want below:\n1:create\t2:read all\t3:read by condition\t4:exit\nprompt> ")
    if select_menu == '1': #create
        create()
    elif select_menu == '2':   #read all
        read_all(face_dict)
    elif select_menu == '3':   #read by condition
        read_by_condition(face_dict)
    elif select_menu == '4':   #exit
        break
    else:
        print("Invalid menu number!")





#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
# def create():
#     global face_list
#     element = Facebook(input("What's your first name?"), input("What's your last name?"),
#                        input("What's your mobile phone number?"), input("What's your email address?"))
#     face_list.append(element)
#
# def read_all(face_list):
#     for e in face_list:
#         e.printAll()
#         print('None\n')
#
#
# def read_by_condition(face_list):
#     keyword = input('keyword> ')
#     element_dict = {}
#     for e in face_list:
#         #key값으로 face_list의 인덱스를 줌
#         element_dict[face_list.index(e)] = {'first_name':e.first_name, 'last_name':e.last_name, 'mobile':e.mobile, 'email':e.email}
#     #
#     items_idx_having_keyword = []
#     for k, v in element_dict.items():
#         # keyword 부분일치인 경우
#         if keyword in v['first_name'] or keyword in v['last_name'] or keyword in v['mobile'] or keyword in v['email']:
#             items_idx_having_keyword.append(k)
#         #
#         # # keyword 완전일치인 경우
#         # if v['first_name'] == keyword or v['last_name'] == keyword or v['mobile'] == keyword or v['email'] == keyword:
#         #     keyword_y_items_idx.append(k)
#     #
#     print('There is(are) %s item(s).' % len(items_idx_having_keyword))
#     for i in items_idx_having_keyword:
#         face_list[i].printAll()
#         print('None\n')
#
# #---------------------------------------------------------------------------------------
#
# face_list = []
#
# while True: #무한 루프
#     select_menu = input("Choose the menu you want below:\n1:create\t2:read all\t3:read by condition\t4:exit\nprompt> ")
#     if select_menu == '1': #create
#         create()
#     elif select_menu == '2':   #read all
#         read_all(face_list)
#     elif select_menu == '3':   #read by condition
#         read_by_condition(face_list)
#     elif select_menu == '4':   #exit
#         break
#     else:
#         print("Invalid menu number!")

