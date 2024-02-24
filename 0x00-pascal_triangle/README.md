0. Pascal's Triangle
mandatory
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer

guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$


When solving the problem of generating Pascal's Triangle up to the nth row in an interview, it's essential to follow a systematic approach. Here's a step-by-step guide:

Understand the Problem:

Clearly understand the problem statement. In this case, you need to generate Pascal's Triangle up to the nth row.
Handle Edge Cases:

Check for edge cases and handle them appropriately. In this problem, an edge case is when 
�
n is less than or equal to 0. In such cases, the function should return an empty list.
Initialize Data Structure:

Start by initializing the data structure that will store the triangle. In this case, you can use a list of lists.
Generate Rows:

Use a loop to generate each row of Pascal's Triangle.
Start with the first row, which is always [1].
For each subsequent row, calculate the values based on the previous row.
Use Nested Loops:

Utilize nested loops for iterating through rows and elements within each row.
Calculate Values:

For each row, calculate the values by summing the corresponding elements from the previous row.
Append Rows:

Append each generated row to the data structure (list of lists) that represents Pascal's Triangle.
Handle the Last Element:

Ensure that each row ends with the value 1.
Return Result:

Return the final result, which is the list of lists representing Pascal's Triangle up to the nth row.
Test with Examples:

After implementing the function, test it with different values, including edge cases, to ensure it produces the correct results.
Optimization (Optional):

If time allows, consider whether there are any optimizations that can be made to the code, such as reducing unnecessary calculations.
Discuss Complexity:

Be prepared to discuss the time and space complexity of your solution. In the case of Pascal's Triangle, the time complexity is typically O(n^2) due to the nested loops.
Remember, communication is crucial during interviews. Explain your thought process, discuss your approach with the interviewer, and seek feedback. It's okay to take your time and ensure a correct and efficient solution. 
