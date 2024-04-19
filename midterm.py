class Star_Cinema:
    hall_list = []
    def __init__(self) -> None:
        pass
    def _entry_hall(self,my_hall):
        self.hall_list.append(my_hall)



class Hall(Star_Cinema):
    def __init__(self, rows,cols,hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self._entry_hall(self)
        super().__init__()

    def entry_show(self,id,movie_name,time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        my_show = (id,movie_name,time)
        flag = True

        for show in self.__show_list:
            if(show[0] == id):
                flag= False

        if flag:
            self.__show_list.append(my_show)
            seat_list = [[0 for i in range(0,self.__cols)] for j in range(0,self.__rows) ]
            self.__seats[id] = seat_list
        else:
            print(f'\n\t{id} already available in show')

    def book_seats(self,id,seat_info):

        if id not in self.__seats:
            print("\n\tSorry, the show id is invalid")

        else:
            for seat in seat_info:
                if 0<=seat[0]<=self.__rows and 0 <= seat[1]<= self.__cols:
                    
                    if self.__seats[id][seat[0]][seat[1]] == 0:
                        self.__seats[id][seat[0]][seat[1]] = 1
                        print(f'\n\tseat booked succesfull. you seat location is {seat[0]},{seat[1]}')
                    else:
                        print(f'\n\tseat already booked, try another seat')
                else:
                    print('\n\tinvalid seat number')

    def view_show_list(self):
        if self.__show_list.__len__() == 0:
            print('\n\tno show is running')
            return
        for show in self.__show_list:
            print(f'\n\tcurrently showing movie is >> {show[1]}, id is>> {show[0]}, time is>> {show[2]}')

    def view_available_seats(self,id):
        if id not in self.__seats:
            print("\n\tSorry, the show id is invalid")
            return
        
        flag = False
        for i in range(0,self.__rows):
            for j in range(0,self.__cols):
                if(self.__seats[id][i][j] == 0):
                    flag = True
                    print(f"[{i},{j}]",end=' ')
                else:
                    print(f'[ X ]',end=' ')
            print('\n')

        if flag:
            print('\n\tthese seats are available.The result are shown in [row,col] format')
            print('\n\t[ X ] means this sit is booked')
        else:
            print('\n\tno seats are available right now')


my_cinema = Hall(8,8,1)
my_cinema.entry_show(1,'jawan','2024-10-05')
my_cinema.entry_show(2,'dhoom','2023-10-05')
my_cinema.entry_show(3,'poran','2022-1-05')
my_cinema.entry_show(4,'jibon','2022-10-09')

run = True

while run:
    print('--------------------------------------')
    print("Option 1: Book a seat")
    print("Option 2: View show list")
    print("Option 3: View available seats")
    print("Option 4: Break")
    print('--------------------------------------')
    
    op = int(input("Enter an option: "))
        
    if op ==1:
        id = int(input('Enter a movie id(must be integar): '))
        row = int(input('Enter a row no of seat: '))
        col = int(input('Enter col no of seat: '))
        seat_info = [(row,col)]
        my_cinema.book_seats(id,seat_info)
    elif op ==2:
        my_cinema.view_show_list()
    elif op ==3:
        id = int(input('Enter a movie id(must be integar) to see available seat: '))
        my_cinema.view_available_seats(id)
    elif op ==4 :
        run = False



