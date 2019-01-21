# K-th ancestor of a node in Binary Tree

Assume you are given a tree of N nodes. The nodes are numbered from 0 to N−1 and their parents are represented in an array A, such that A[i] denotes the number of the parent of the i-th node. Node 0 is the root node and it will not have a parent, so the corresponding value in array A will be −1. We define the distance between two nodes to be the length of the shortest path between them, and we define an ancestor of the i-th node as any node lying on the shortest path between the i-th node and the root. Your goal is to find the ancestor at distance D of every node of the tree.

function solution(D, A);

that, given an integer D and array A of N integers, returns an array of N integers representing the ancestors at distance D of the consecutive nodes. If a node doesn't have an ancestor at distance D its field should contain −1.

For example, given integer D = 2 and array A such that:

A[0] = -1
A[1] = 0
A[2] = 4
A[3] = 2
A[4] = 1

your function should return [−1, −1, 0, 1, −1].

the first element of array A equals −1;
array A represents a valid tree.

![Reference www.chegg.com](https://media.cheggcdn.com/media%2F0e9%2F0e967511-3fed-4d42-a9a2-0d9231a91ea9%2FphpqnbQLj.png)
