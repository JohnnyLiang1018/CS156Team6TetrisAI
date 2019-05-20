
class kb(object):

    task = ""
    param = ""
    current_shape = ""

    # shape representation
    I_shapeCoord = (
        (0,0),(0,1),(0,2),(0,3)
    )
    
    T_shapeCoord = (
        (0,0),(0,1),(-1,1),(1,1)
    )

    O_shapeCoord = (
        (0,0), (0,1), (1,0), (1,1)
    )

    S_shapeCoord = (
        (0,0), (0,1), (-1,1), (-1,2)
    )

    L_shapeCoord = (
        (0,0), (0,1), (0,2), (1,0)
    )

    Z_shapeCoord = (
        (0,0), (0,1), (1,1),(1,2)
    )

    J_shapeCoord = (
        (0,0), (1,0), (1,1), (1,2)
    )

    # current_board 10*10, 0 means empty and 1 means filled
    board = (
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    )
    height = 0
    holes = 0

    def __init__(self):
        print("KB initialize")

    def kb_ask(self,request):
        self.task = request[0]
        self.param = request[1]
        print("Handling request " + self.task)
        self.request_handle()

    def update_board (self):
        self.current_shape = self.param[0]
        location_x = self.param[1][0]
        # print("Location_x: " + str(location_x))
        location_y = self.param[1][1]
        # print("Location_y: " + str(location_y))
        shape = self.getCurrentShape()
        for point in shape:
            for xy in range(len(point)):
                if(xy == 0):
                    x_value = point[0]
                else:
                    y_value = point[1]
            # print("Updating at x: " + str(location_x + x_value))
            # print("Updating at y: " + str(location_y + y_value))
            self.board[len(self.board) - 1 - location_y - y_value][location_x + x_value] = 1
        
    def check_row_clear (self,row_num):
        for value in self.board[len(self.board) -1 -row_num]:
            if(value != 1):
                return False
        return True

    def remove_row (self,row_num):
        print("Removing row(fact) ")
        row = len(self.board) -1 - row_num
        print("row " + str(row))
        for xy in range(len(self.board[row])):
            self.board[row][xy] = 0
            

    def request_handle(self):
        if (self.task == "update_board"):
            print("Updating board(fact)")
            self.update_board()
            for row in self.board:
                print(row)

        if (self.task == "add_shape"):
            self.current_shape = self.param
            print("Adding shape(rule) " + self.current_shape)
            print(self.add_shape())
        
        if (self.task == "remove_shape"):
            self.current_shape = self.param
            print("Removing shape(rule) " + self.current_shape)
            print(self.remove_shape())
        
        if (self.task == "remove_row"):
            self.remove_row(self.param)
            for row in self.board:
                print(row)
        
        if (self.task == "display_board"):
            for row in self.board:
                print(row)
            return self.board

        if (self.task == "set_board"):
            self.board = self.param
            for row in self.board:
                print(row)
            


    def add_shape(self):
        if (self.current_shape == "L"):
            self.L_shapeCoord = (
                (0,0), (0,1), (0,2), (1,0)
            )
            return self.L_shapeCoord
        if (self.current_shape == "I"):
            self.I_shapeCoord = (
                (0,0),(0,1),(0,2),(0,3)
            )
            return self.I_shapeCoord
        if (self.current_shape == "O"):
            self.O_shapeCoord = (
                (0,0), (0,1), (1,0), (1,1)
            )
            return self.O_shapeCoord
        if (self.current_shape == "S"):
            self.S_shapeCoord = (
                (0,0), (0,1), (-1,1), (-1,2)
            )
            return self.S_shapeCoord
        if (self.current_shape == "Z"):
            self.Z_shapeCoord = (
                (0,0), (0,1), (1,1),(1,2)
            )
            return self.Z_shapeCoord
        if (self.current_shape == "J"):
            self.J_shapeCoord = (
                (0,0), (1,0), (1,1), (1,2)
            )
            return self.J_shapeCoord
        if (self.current_shape == "T"):
            self.T_shapeCoord = (
                (0,0),(0,1),(-1,1),(1,1)
            )
            return self.T_shapeCoord
    
    def remove_shape(self):
        if (self.current_shape == "L"):
            self.L_shapeCoord = (
                
            )
            return self.L_shapeCoord
        if (self.current_shape == "I"):
            self.I_shapeCoord = (
              
            )
            return self.I_shapeCoord
        if (self.current_shape == "O"):
            self.O_shapeCoord = (
            
            )
            return self.O_shapeCoord
        if (self.current_shape == "S"):
            self.S_shapeCoord = (
             
            )
            return self.S_shapeCoord
        if (self.current_shape == "Z"):
            self.Z_shapeCoord = (
             
            )
            return self.Z_shapeCoord
        if (self.current_shape == "J"):
            self.J_shapeCoord = (
            
            )
            return self.J_shapeCoord
        if (self.current_shape == "T"):
            self.T_shapeCoord = (
            
            )
            return self.T_shapeCoord


    # Return current shape in an array, starting from the center (0,0), and dot
    # location in (x,y) in respect to the center
    def getCurrentShape(self):
        if (self.current_shape == "L"):
            return self.L_shapeCoord
        if (self.current_shape == "I"):
            return self.I_shapeCoord
        if (self.current_shape == "O"):
            return self.O_shapeCoord
        if (self.current_shape == "S"):
            return self.S_shapeCoord
        if (self.current_shape == "Z"):
            return self.Z_shapeCoord
        if (self.current_shape == "J"):
            return self.J_shapeCoord
        if (self.current_shape == "T"):
            return self.T_shapeCoord

    def getRotateShape(self):
        return None

    def getCurrentHeight(self):
        return None

    def getCurrentSurface(self):
        return None

