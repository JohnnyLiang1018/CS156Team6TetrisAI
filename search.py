class search:

    stateList = (
        (x,y,rotate_num),
        (x_1,y_1,rotate_num)
    )

    def weightCalculate(self,stateList):
        return None



    def solutionSearch(self,weightList):

        max_weight_index = None
        max_weight = 0

        for i in range(len(weightList)):
            current_weight = weightList[i]
            if (current_weight > max_weight):
                max_weight_index = i
                max_weight = current_weight
        
        return max_weight_index
    

            

            