#!/usr/bin/env python
'''
function solution(D, A): Given an integer D and array A of N integers, 
   returns an array of N integers representing the ancestors at distance D of the consecutive nodes. If a node doesn't have an ancestor at distance D its field should contain −1
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
def at_root(element):
    if element==0 or element==-1:
        return True

    return False


def solution(D, A):
    adict = list_to_dict(A)
    array = []
    for element in A:
        print("Node..",element)        
        if at_root(element):
            print("Already at root skipping..Outside loop")
            array.append(-1)
            print(array)
            continue
        current_node=element        
        for itr in range(D):            
            ancestor=adict[current_node]                       
            print("D=",itr,"A[",current_node,"]->",ancestor)
            if at_root(ancestor):
                print("Already at root skipping..Inside loop")
                #array.append(-1)
                array.append(-1)
                continue            
            current_node=ancestor
        array.append(ancestor)
        print(array)
    
        

def main():
    #anum = int(input("Please enter a number"))
    D=2 # integer D
    A=[-1, 0, 4, 2, 1] # array A of N integers
    solution(D,A)

if __name__ == "__main__":
    main()