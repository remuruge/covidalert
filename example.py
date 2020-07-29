from datetime import datetime

userList = [{"userId": 1, "name": "Stephen Brennan", "email": "StephenBrenann@gmail.com","address": "5 St. Powers Walk Cresent", "phone": "0851180846", "accountNo": "0000001"},
            {"userId": 2, "name": "Alex Smith", "email": "AlexSmith@gmail.com", "address": "5 St. Powers Walk Cresent","phone": "0851183546", "accountNo": "0000002"},
            {"userId": 3, "name": "David Jones", "email": "DavidJones@gmail.com","address": "5 St. Powers Walk Cresent", "phone": "0852580846", "accountNo": "0000003"},
            {"userId": 4, "name": "Wellington Waters V", "email": "damian.lockman@gmail.com", "address": "5135 Bartoletti Lodge Suite 372 Ebertburgh, WI 78211", "phone": "1000079613","accountNo": "1013507"},
            {"userId": 5, "name": "Antone Kautzer III", "email": "mayert.hollie@gmail.com", "address": "29634 White Curve Apt. 446 East Nikolas, AL 28572", "phone": "1000020243", "accountNo": "1050581"},
            {"userId": 6, "name": "Prof. Gerald Williamson", "email": "yasmin81@gmail.com", "address": "1084 Ella Point Suite 506 Karinebury, WV 32343-7303", "phone": "1000084822", "accountNo": "1057896"},
            {"userId": 7, "name": "Mrs. Destiny Bogan PhD", "email": "gerlach.jeanett@gmail.com", "address": "7844 Kilback Common New Consuelo, IN 01019", "phone": "1000006060", "accountNo": "1070956"},
            {"userId": 8, "name": "Libby Roberts", "email": "elyse57@gmail.com", "address": "8516 Carter Dale Apt. 211 Walkerland, AZ 37809-7356", "phone": "1000053367", "accountNo": "1040506"},
            {"userId": 9, "name": "Brendan Rau", "email": "tamia.torp@gmail.com", "address": "30766 Osbaldo Union Apt. 063 New Leoview, NJ 78208-7355", "phone": "1000057713", "accountNo": "1050992"},
            {"userId": 10, "name": "Prof. Easter Sipes", "email": "jonathan.wyman@gmail.com", "address": "22587 Nelson Vista Suite 809 North Kris, UT 57011-6075", "phone": "1000081369", "accountNo": "1023142"},
            {"userId": 11, "name": "Jeanne Paucek", "email": "braeden33@gmail.com", "address": "3845 Schinner Fort North Laneshire, ME 55598", "phone": "1000088943", "accountNo": "1068818"},
            {"userId": 12, "name": "Mrs. Estefania Romaguera", "email": "veronica62@gmail.com", "address": "8878 Zora Wall Apt. 524 New Velmamouth, WI 17074-8689", "phone": "1000075419", "accountNo": "1054956"},
            {"userId": 13, "name": "Talia Altenwerth", "email": "araceli24@gmail.com", "address": "6951 Reichel Knoll Elyssaborough, NV 80639", "phone": "1000024379", "accountNo": "1008242"},
            {"userId": 14, "name": "Kelly Hammes", "email": "mckenzie.tracy@gmail.com", "address": "42685 Lynch Court Vivianeborough, UT 51230-6238", "phone": "1000024443", "accountNo": "1030633"},
            {"userId": 15, "name": "Mr. Trenton Will DVM", "email": "jaskolski.addie@gmail.com", "address": "6228 Amparo Ridges Suite 658 East Clyde, IL 62176-1774", "phone": "1000007174", "accountNo": "1005685"},
            {"userId": 16, "name": "Rory Jenkins", "email": "franz32@gmail.com", "address": "7943 Quincy Overpass Apt. 581 Hillsfurt, KS 22616", "phone": "1000065732", "accountNo": "1002568"},
            {"userId": 17, "name": "Buck Padberg MD", "email": "bode.forrest@gmail.com", "address": "81012 Murazik Valleys Melynafurt, NY 00145-7298", "phone": "1000089025", "accountNo": "1078788"},
            {"userId": 18, "name": "Lonnie Will", "email": "isaac.legros@gmail.com", "address": "2001 Runte Inlet Apt. 176 Easterland, RI 22292", "phone": "1000067727", "accountNo": "1036567"},
            {"userId": 19, "name": "Jaeden Ledner", "email": "finn.heller@gmail.com", "address": "04236 Roosevelt Centers Apt. 631 Port Hazel, TX 01233-0470", "phone": "1000047791", "accountNo": "1046300"},
            {"userId": 20, "name": "Mabel Gerlach III", "email": "oschroeder@gmail.com", "address": "683 Ezequiel Meadow Hoppeview, DE 94432", "phone": "1000073590", "accountNo": "1033236"}]
userVisits = [{"visitId": 1, "userId": 1, "branchId": 1, "date": "2020-07-28T00:00:00.000Z"},
              {"visitId": 2, "userId": 1, "branchId": 2, "date": "2020-07-28T00:00:00.000Z"},
              {"visitId": 3, "userId": 2, "branchId": 1, "date": "2020-07-28T00:00:00.000Z"},
              {"visitId": 4, "userId": 3, "branchId": 2, "date": "2020-07-28T00:00:00.000Z"},
              {"visitId": 5, "userId": 4, "branchId": 1, "date": "2020-07-28T00:00:00.000Z"},
              {"visitId": 6, "userId": 5, "branchId": 1, "date": "2020-07-28T00:00:00.000Z"},
              {"visitId": 7, "userId": 6, "branchId": 2, "date": "2020-07-29T00:00:00.000Z"}]

def get_aymptomatic(email):
    flag = 0

    for user in userList:
        if user['email'] == email:
            flag = 1
            keyUserVisit = [(visit['branchId'],visit['date'],visit['userId']) for visit in userVisits if visit['userId'] == user['userId']]
            print(keyUserVisit)
            for (visitBranch, visitDt, keyUserId) in keyUserVisit:
                usersIdentified = [visits for visits in userVisits if (visits['branchId'] == visitBranch and datetime.strptime(visits['date'],"%Y-%m-%dT%H:%M:%S.%fZ") == datetime.strptime(visitDt,"%Y-%m-%dT%H:%M:%S.%fZ"))]
                aymptUsers=filter_keyUser(usersIdentified,keyUserId)
                print(get_user(aymptUsers))
    if flag == 0:
            print('Invalid user ' + email)

def get_user(users):
    asymptomatic_users=[]
    for u in users:
        for user in userList:
            if user['userId'] == u['userId']:
                u['name']=user['name']
                u['email']=user['email']
                u['address']=user['address']
                u['phone']=user['phone']
        asymptomatic_users.append(u)
    return asymptomatic_users

def filter_keyUser(usersIdentified,keyUserId):
    maybeInfected = [user for user in usersIdentified if user['userId'] != keyUserId]
    return maybeInfected

if __name__ == '__main__':
    get_aymptomatic('StephenBrenann@gmail.com')