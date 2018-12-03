// Strahinja Trecakov
// CIBC Developer Tasks: Required task 2
// 12/02/18
//
// Implement a CircularArray class in C++ that supports an array-like data
// structure which can be efficiently rotated. If possible, the class should be
// generic and support iteration via the range-based for loop of C++11. Write a
// driver program in C++ (i.e., a main() function) that demonstrates your class's
// capabilities in various ways. Summarize briefly how this system could be tested.
 

#ifndef CIRCULARARRAY_H_
#define CIRCULARARRAY_H_

#include <iostream>
#include <string>
using namespace std;

template <class T> 
class circularArray 
{
    private:
    	int size;
    	T *arr;
    
    public:
         //constuctors
   	 circularArray(int s) 
	 {
         	size = s;
                arr = new T [size];
         }//default one
    
    	 circularArray(int s, int a[])
	 {
                size = s;
                arr = new T [size];
   	 	for(int i = 0; i < size; i++)
        		arr[i] = a[i];
         }//int

	 circularArray(int s, float a[])
	 {
                size = s;
                arr = new T [size];
                for(int i = 0; i < size; i++)
                        arr[i] = a[i];
         }//float

	 circularArray(int s, char a[]) 
	 {
                size = s;
                arr = new T [size];
                for (int i = 0; i < size; i++)
                        arr[i] = a[i];
         }//char

	 //funcitons
    	void add_to_array(int size); 
    	void print_array(int size); 
    	void clockwise(int start, int size); 
    	void anticlockwise(int start, int size); 
};

//add elements into an array
template <class T> 
void circularArray<T>::add_to_array(int size) 
{    
    cout << "Enter the elements of the circularArray" << endl;
    for (int i = 0; i < size; i++)
        cin >> arr[i];
    cout << endl;
}//add_to_array

//print array
template <class T>
void circularArray<T>::print_array(int size)
{
    for (int i = 0; i < size ; i++)
            cout << arr[(i % size)] << " ";
    cout << endl;
}//print_array

//print array rotated clockwise
template <class T> 
void circularArray<T>::clockwise(int start, int size)
{
    for (int i = start; i < size + start; i++)
            cout << arr[(i % size)] << " ";
    cout << endl;
}//clockwise

//print array rotated anticlockwise
template <class T> 
void circularArray<T>::anticlockwise(int start, int size)
{
    for(int i = size + start; i > start; i--)          
            cout << arr[(i % size)] << " ";
    cout << endl;
}//anticlockwise

#endif
