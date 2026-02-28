class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
            Time: O(n*m)
            Space: O(n*m)
            NOTE: You can't just calculate at each node if it is capturable or not,
            because if you calculate it per node and mark the node before checking all the possible connections from it,
            then you may mark a node wrong because it is possible for a node to turn out to be opposite of your earlier marking.
            THE CASE here is to CHECK ALL THE POSSIBLE CONNECTED NODES(CONNECTED COMPONENT) AND
            THEN MARK ALL THE NODES IN THERE AS X OR O DEPENDING UPON WHAT YOU FOUND IN ONE FULLY CONNECTED COMPONENT
        '''


        '''
            Recurisve solution using DFS
        '''
        self.n = len(board)
        self.m = len(board[0])
        if self.n < 3 or self.m < 3:
            return board
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = set()
        component = []
        
        def move(i, j):
            if (i == 0 or i == self.n - 1 or j == 0 or j == self.m - 1):
                return False
            
            capture = True
            component.append((i, j))
            vis.add((i, j))
            
            for dir_i, dir_j in dirs:
                new_i, new_j = i + dir_i, j + dir_j
                if -1 < new_i < self.n and -1 < new_j < self.m and (new_i, new_j) not in vis:
                    if board[new_i][new_j] == "O":
                        res = move(new_i, new_j)
                        capture = capture and res
            
            return capture

        def mark(component):
            for i, j in component:
                board[i][j] = "X"


        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (i, j) in vis:
                    continue
                component = []
                if board[i][j] == "O" and move(i, j):
                    mark(component)
        

        
        return board


        '''
            Border DFS solution
            Time: O(n*m)
            Space: O(1)
            NOTE: The idea is to start from the borders and mark all the nodes that are connected to the borders as S,
            then in the end we can mark all the S nodes as O and all the rest as X,
            because all the S nodes are not capturable and all the rest are capturable

            Also, when parsing first row and last row, we can do it in one loop and the same goes for first and last column
            Also, you don't necessarily need dirs array, you can just call the function for all dirs manually
        '''
        self.n = len(board)
        self.m = len(board[0])
        if self.n < 3 or self.m < 3:
            return board
        
        def move(i, j):
            # only process if i, j are in bounds and current node is O
            if -1 < i < self.n and -1 < j < self.m and board[i][j] == "O":

                # mark the current node
                board[i][j] = "S"
                
                # check all the possiblities from here
                move(i, j + 1)
                move(i, j - 1)
                move(i + 1, j)
                move(i - 1, j)
        
        # first and last column check
        for i in range(self.n):
            move(i, 0)
            move(i, self.m - 1)

        # first and last row check 
        for i in range(self.m):
            move(0, i)
            move(self.n - 1, i)

        # final cleaning
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
        return board


        '''
            Iterative solution using stack
        '''
        # self.n = len(board)
        # self.m = len(board[0])
        # if self.n < 3 or self.m < 3:
        #     return board
        
        # dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # vis = set()
        
        # def move(i, j):
        #     capture = True
        #     stk = [(i, j)]
        #     component = []
        #     capture = True
            
        #     while stk:
        #         i, j = stk.pop()

        #         if (i == 0 or i == self.n - 1 or j == 0 or j == self.m - 1):
        #             capture = False

        #         if (i, j) in vis:
        #             continue

        #         component.append((i, j))
        #         vis.add((i, j))
        #         for dir_i, dir_j in dirs:
        #             new_i, new_j = i + dir_i, j + dir_j
        #             if -1 < new_i < self.n and -1 < new_j < self.m and (new_i, new_j) not in vis:
        #                 if board[new_i][new_j] == "O":
        #                     stk.append((new_i, new_j))
            
        #     return component, capture

        # def mark(component):
        #     for i, j in component:
        #         board[i][j] = "X"


        # for i in range(1, self.n - 1):
        #     for j in range(1, self.m - 1):
        #         if (i, j) in vis:
        #             continue
        #         if board[i][j] == "O":
        #             component, capture = move(i, j)
        #             if capture:
        #                 mark(component)
    
        # return board