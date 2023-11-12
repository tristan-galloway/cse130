GET number

SET list_nums <- [number]
SET francois_number <- 0

WHILE list_nums is not empty                        

    num <- list_nums[0]                             #A

    IF num > 2                                      #B
        append num - 1 and num - 2 to list_nums     

    ELSE IF num = 2                                 #C
        francois_number + 1

    ELSE IF num = 1                                 #D
        francois_number + 2

    REMOVE list_nums[0] in list_nums                #E

PUT The number is francois_number                   #F