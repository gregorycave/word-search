
def main():
    """
    the main body of the program
    is simply used to first
    display the grid to the user
    and then in turn the menu

    after this has been done,
    the user is asked to make
    a choice to search through
    the grid to find a word

    this is achieved through
    calling the search grid
    function of the program
    """
    print("")

    finished=False
    valid=False
    choices=["1", "2", "3"]

    grid=load_grid()

    print("")

    for line in grid:
        print(line)
        
    while not valid:   
        while not finished:
            print("\n***MAIN MENU***")
            print("\n1.) Load a text file to search the grid.")
            print("2.) Manually search for a word in the grid.")
            print("3.) Quit the program.")
            
            choice=input("\nPlease select an option: ")
            
            if choice in choices:
                valid=True
                if choice=="1":
                    words=load_words()
                    print("")
                    for word in words:
                        found=search_grid(grid, word)
                        if word=='':
                            pass
                        else:
                            if found==False:
                                print("{0} was not found in the grid!".format(word))
                            else:
                                print("{0} found: {1} to {2} from row {3} col {4}".format(found[0], found[1], found[2], found[3], found[4]))
                            
                elif choice=="2":
                    word=input("\nPlease enter a word to search for: ")
                    if found==False:
                        print("{0} was not found in the grid!".format(word))
                    else:
                        print("{0} found: {1} to {2} from row {3} col {4}".format(found[0], found[1], found[2], found[3], found[4]))
                else:
                    finished=True
            else:
                print("Invalid input! Please try again.")


def search_grid(grid, word):
    """
    the search grid function
    makes up the majority
    of the program

    it is called from the main
    function of the program,
    and is used to first store
    the grid in different ways
    e.g. vertically, horizontally
    right-left, down-up etc.

    it will then return the word
    that has been found, as well
    as the orientation of the word
    within the grid along with its
    associated column and row.
    """
    grid_lr=[]
    grid_rl=[]
    grid_ud=[]
    grid_du=[]

    for line in grid:
        grid_lr.append(line)
        grid_rl.append(line[::-1])

    for each in range(0, len(grid[0])):
        line_ud=[]

        for line in grid:
            line_ud.append(line[each])

        line_ud=''.join(line_ud)
        grid_ud.append(line_ud)      
        grid_du.append(line_ud[::-1])

    finished=False
    
    while not finished:
        
        for line in grid_lr:
            if word in line:
                found=[word, "left", "right", (grid_lr.index(line)+1), (line.index(word)+1)]
                finished=True
        for line in grid_rl:
            if word in line:
                found=[word, "right", "left", (grid_rl.index(line)+1), (abs(line.index(word)-len(line)))]
                finished=True
        for line in grid_ud:
            if word in line:
                found=[word, "up", "down", (line.index(word)+1), (grid_ud.index(line)+1)]
                finished=True
        for line in grid_du:
            if word in line:
                found=[word, "down", "up" , (abs(line.index(word)-len(line))), (grid_du.index(line)+1)]
                finished=True

        if finished==False:
            found=False

        return found

def load_words():
    """
    this is a simple function
    used to load the search
    terms for option 1 in the
    main body of the program
    """
    valid=False
    while not valid:
        filename=input("\nEnter a filename for search terms: ")
        try:
            words = [line.rstrip('\n') for line in open(filename)]
            valid=True
        except:
            pass

    return words


def load_grid():
    """
    this is a simple function
    used to load the contents
    of the grid to be displayed
    in the main body of the program
    """   
    valid=False
    while not valid:
        filename=input("\nEnter a filename for the text grid: ")
        try:
            grid = [line.rstrip('\n') for line in open(filename)]
            valid=True
        except:
            pass

    return grid
        

if __name__ == '__main__':
    
    main()
    
