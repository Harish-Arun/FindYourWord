FIND YOUR WORD

PROBLEM STATEMENT:

Efficient way to search for words in a document using trees as the data structures for the search algorithms.

It is customary to take loads of manual time and labor for searching of words/keywords in a document. An efficient and comfortable approach to this inconvenience is to have a word searcher to find the required keywords/words in the given document or any other case with this issue. 

APPROACH:

	We propose on implementing this through the data structure “TREE”. The Tree of choice for implementing our problem is by using AVL trees. The reason of choosing AVL trees is that this tree has the best search time complexity comparing the other tree structures available to us. 

This application first segregates the words using the size of those words as small letters are accessed more frequently than others. This segregation is done based on the AVL trees. By creating nodes of these tree with size of the word as key, those nodes will have an inner tree in which the original words are sorted based on existing AVL algorithm.

As they are first classified based on the number of size and then with the words, the search timing for the problem statement will be reduced drastically. 

For example, 

	Let’s have a word “Hello” to be searched in a document. The program first checks the size of the input then goes to the appropriate node which have the key as 5. After reaching the node 5, the node will have a AVL tree in which the words are stored. It searches for the node where “Hello” is present. If that node 5 have the node “Hello” it will be found and shows where this word presents in the document.

Contributions:
Harish A
Prajeeth B
