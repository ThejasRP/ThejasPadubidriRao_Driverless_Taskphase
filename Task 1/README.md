# Problem Statements

Q1. Input an integer n, input n strings into a list. Create a dictionary where the key is an alphabet and the value is how many times it appears across all the strings. Not case sensitive. Eg for ["Formula", "Manipal"] the output looks like {'f':1, 'o':1, 'a':3 ...}.

Q2. Create a class with a function that does selection sort on a list of strings. Input a list like Q1, call the function, print the output.

Q3. Create a class with a function that does binary search in a list of strings. Input a list like Q1, sort it using your Q2 function, input a string, search for it.

Q4. Write a function for matrix multiplication. It should support any dimensions and print errors where multiplication is impossible.

Q5. Learn open hashing. Implement a hash table using 2D lists. Input n integers. Every number where num % 10 == 0 goes in sublist 0,  num % 10 == 1 goes in sublist 1, and so on. Print the hash table.

Q6. Improve Q5. Insert each new number so the sublist stays sorted. Do not sort after insertion. Hint, find the insertion index using binary search.

Q7. Let (x,y) be a point in 2D space. Given a list of coordinates, write a sort function that sorts them by proximity to a reference point given by the user that is not in the list. Eg list [(0,1),(0,3),(1,2)], reference (0,0), output [(0,1),(1,2),(0,3)].

Q8. Consider a CSV ( cones.csv ) with cone id, x, y, colour (blue or yellow) per row. Sort the rows by distance from the origin. Write two new CSVs, one per colour, keeping the sorted order. Then find the midpoint between every blue cone and its nearest yellow cone and write those midpoints to centreline.csv.

## Resources:
Python Docs
Python Basics from W3 Schools
Python File Handling from W3 Schools 
Hash Tables from HackerEarth