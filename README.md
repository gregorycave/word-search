# word-search
A word search program built using Python that searches for words in a grid using a text file

This program is used to solve word search puzzles. For example in the following word grid it is possible to find the words active, stock, ethernet and java.

```
xmmycxvtljlqbbybkoumjqwbtbufve
buubmekxbeydqmcnzyjpvdankomdmi
lqactivexnyvwdvcoshoyrohgvfvqj
vsewohvnbxsduqjiffkoyhpdwbrngc
dvqwwwfkoyamapmlrrjvtkljpcvkua
iqqfxtumsjvfmtrsbycyqiarixqikp
afgrvlqzdqaxaoanfqplmjpjhnzams
yofywrbpfcjiflcbbcoecxpwljyuyt
twyxetyuyufvvmcuawjmbwlqhxjgqo
txekdexmdbtgvhpyvsqtmljdxeqltc
dcctenrehteoxqdgnueljtrrnesgok
oqsnakqwerouftmgnjqbytjzhmwncc
```

The user is prompted for a filename, and then the program will attempt to open the file whose name is supplied. If the file cannot be opened the user is asked to supply another filename; this should continue until a file has been successfully opened.

The file contains on each line a row from the grid. For example the first two lines of a file that contains the grid shown on the previous page would be

```
xmmycxvtljlqbbybkoumjqwbtbufve
buubmekxbeydqmcnzyjpvdackomdmi
```

## Inputting the Grid from a File

The program will read, in turn, each line of the file, remove the newline character and append the resulting string to a list of strings.

After the input is complete the strings in the list will be displayed on the screen, one per line.

Note that grids used for testing the submitted programs may have different widths and heights from the sample one that will be provided. Grids will contain only lower-case letters.

## The Word-Search Function

The function that will take two arguments: a word to be searched for and a list of strings containing the grid.

The function searches for a horizontal (left-to-right or right-to-left) or vertical (downwards or upwards) occurrence of the word. If a word occurs more than once the function is required to find only one occurrence so it will stop searching once the word has been found.

If the word has not been found 'None' is returned; if the word has been found the function returns a tuple, containing the row and column numbers of the first letter of the word and a string indicating the direction (i.e. four integers). The top row will be
regarded as row 1 and the leftmost column as column 1.

## The Word-Search

After displaying the grid, the program asks the user to supply a name of a file containing words to be searched for, one word per line. This file should be opened, once again asking the user to supply another name if necessary. The program supplies each word in this file in turn to the word-search function. If the function returns 'None' the word is added to a list of words that have not been found; otherwise the tuple returned is added to a dict object using the word as a key.

After searching for all of the words the program will display details of all of the words in the dictionary (in alphabetical order) using a format such as
```
 active found: left to right from row 3 col 3
 ```
 
Finally, the program will output a list of the words that were not found (also in alphabetical order).
