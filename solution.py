#!/usr/bin/env python
'''
function solution(D, A): Given an integer D and array A of N integers, 
   returns an array of N integers representing the ancestors at distance D of the consecutive nodes. If a node doesn't have an ancestor at distance D its field should contain −1

Usage: supply int D and list A in the main() function

For example, given integer D = 2 and array A such that:

A[0] = -1
A[1] = 0
A[2] = 4
A[3] = 2
A[4] = 1

your function should return [−1, −1, 0, 1, −1].
'''

# function list_to_dict(A): Given an list of N integers
#   returns a dictionary of N integers
def list_to_dict(A):    
    return dict(enumerate(A))    

# function at_root(element): Given an integer
#   returns True if integer is 0 or 1 ie
def isRoot(element):
    if element==0 or element==-1:
        return True
    return False

# function solution(D, A): Given an integer D and array A of N integers, 
#   returns an array of N integers representing the ancestors at distance D of the consecutive nodes. If a node doesn't have an ancestor at distance D its field should contain −1
def solution(D, A):
    adict = list_to_dict(A)
    array = []
    for element in A:
        print("Node..",element)
        current_node = element
        distance = 0        
        while distance < D:            
            if isRoot(current_node):
                print("No ancestor ...")
                ancestor = -1
                print("D=",distance,"A[",current_node,"]->",ancestor)
                break
            else:
                print("D=",distance,"A[",current_node,"]->",ancestor)
                distance += 1
                ancestor=adict[current_node]
                current_node=ancestor
        print("Adding",ancestor)
        array.append(ancestor)
        print(array)
    
        

def main():
    #D = int(input("integer D"))
    D=2 # integer D
    A=[-1, 0, 4, 2, 1] # array A of N integers
    for i in range(len(A)):
        print("A[",i,"]->",A[i])

    solution(D,A)

if __name__ == "__main__":
    main()