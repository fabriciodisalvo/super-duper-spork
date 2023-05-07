
n = 0  # Number of Prisoners
k = 0  # Execution pattern

prisoner_list = []

def generate_list(n):
    prisoner_list = [i+1 for i in range(n)]
    return prisoner_list


def execute_prisoners(n, k):
    prisoner_list = generate_list(n)
    execution_list = []
    remainder = 0
    prisoners_left = True

    while prisoners_left == True:
        # Check if list is shorter than pattern

        if len(prisoner_list) < k:
            for j in range(k-1):
                execution_list.append(prisoner_list.pop(-1))
            print("Execution List:", execution_list, "Remaining list:" ,prisoner_list)
            prisoners_left = False
            return(execution_list[-1])

        # Run a linear pick of prisoners to execute.
        for i in range(k,len(prisoner_list)+1,k):
            execution_list.append(prisoner_list[i-1])
            print("Execution List:", execution_list, "Remaining list:" ,prisoner_list)
        remainder = (len(prisoner_list)%k)
        print("Rem:",remainder)
        prisoner_list = prisoner_list[-remainder:] + prisoner_list[:-remainder]
        print("NEW:", prisoner_list)
        
        # Remove executed prisoner from prisoner list.
        for i in execution_list:
            if i in prisoner_list:
                prisoner_list.remove(i)


def solve_problem(n, k):
    pass

print(execute_prisoners(5, 2))