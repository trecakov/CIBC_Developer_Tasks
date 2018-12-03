// Strahinja Trecakov
// CIBC Developer Tasks: Required task 2
// 12/02/18
//
// Implement a CircularArray class in C++ that supports an array-like data
// structure which can be efficiently rotated. If possible, the class should be
// generic and support iteration via the range-based for loop of C++11. Write a
// driver program in C++ (i.e., a main() function) that demonstrates your class's
// capabilities in various ways. Summarize briefly how this system could be tested.

// Driver class
#include "circularArray.h"

int main()
{
    
    int nth, test, array;
    int size = 0;
    
    cout<< "CircularArray Testing" << endl << "--------------------------------" << endl;
    cout<< "For automated test input 1," << endl << "for user test input 2," << endl << "to exit input 0:" << endl;
    cin >> test;
    
    while(test != 1 && test != 2 && test != 0) 
    {
        cout << "Please input the corrent number" << endl;
    	cin >> test;
    }//while
    
    //automated test
    if(test == 1)  
    {
    	size = 10;
  	nth = 4;
       	int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        float f[] = {1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1};
        char c[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'};
       
        //int array
        circularArray<int> cArray_int(size, a); 
        cout << "Integer circular array: " << endl;
        cArray_int.print_array(size);
        cout << "Clockwise from " << nth << "th index:" << endl;
        cArray_int.clockwise(nth, size);
        cout << "Anticlockwise from " << nth << "th index:" << endl;
        cArray_int.anticlockwise(nth, size);

        //float array
        circularArray<float> cArray_float(size, f);
        cout << "Float circular array: " << endl;
        cArray_float.print_array(size);
        cout << "Clockwise from " << nth << "th index:" << endl;
        cArray_float.clockwise(nth, size);
        cout << "Anticlockwise from " << nth << "th index:" << endl;
        cArray_float.anticlockwise(nth, size);
      
        //char array
        circularArray<char> cArray_char(size, c);
        cout << "Char circular array: " << endl;
        cArray_char.print_array(size);
        cout << "Clockwise from " << nth << "th index:" << endl;
        cArray_char.clockwise(nth, size);
        cout << "Anticlockwise from " << nth << "th index:" << endl;
        cArray_char.anticlockwise(nth, size);
    }//if
    
    //user test
    else if(test == 2) 
    {
        cout << "For int circular array input 1," << endl << "for float circular array input 2," << endl << "and for char circular array input 3:" << endl;
        cin >> array;
        
        while(array != 1 && array != 2 && array != 3) 	
	{
                cout << "Please input the corrent number" << endl;
                cin >> test;
        }//while
        
        //integer array
        if(array == 1) 
	{
            cout << "Integer circular array:" << endl;
            cout << "Enter the size of the circular array (number of elements): " << endl;
            cin >> size;
            circularArray<int> cArray(size);
            cArray.add_to_array(size);
            cout << "Enter the index of rotation (0 to " << size-1 << ")" << endl;
            cin >> nth;
                
            cout << "Clockwise from " << nth << "th index:" << endl;
            cArray.clockwise(nth, size);
            cout << "Anti-clockwise from " << nth << "th index:" << endl;
            cArray.anticlockwise(nth, size);
        }//int cArray
        
        //float array
        else if(array == 2)
	{
            cout << "Float circular array:" << endl;
            cout << "Enter the size of the circular array (number of elements): " << endl;
            cin >> size;
            circularArray<float> cArray(size);
            cArray.add_to_array(size);
            cout << "Enter the index of rotation (0 to " << size-1 << ")" << endl;
            cin >> nth;
            
            cout << "Clockwise from " << nth << "th index:" << endl;
            cArray.clockwise(nth, size);
            cout << "Anti-clockwise from " << nth << "th index:" << endl;
            cArray.anticlockwise(nth, size);
        }//float cArray
        
        //char array
        else if(array == 3)
	{
            cout << "Char circular array:" << endl;
            cout << "Enter the size of the circular array (number of elements): " << endl;
            cin >> size;
            circularArray<char> cArray(size);
            cArray.add_to_array(size);
            cout << "Enter the index of rotation (0 to " << size-1 << ")" << endl;
            cin >> nth;
            
            cout << "Clockwise from " << nth << "th index:" << endl;
            cArray.clockwise(nth, size);
            cout << "Anti-clockwise from " << nth << "th index:" << endl;
            cArray.anticlockwise(nth, size);
        }//char cArray
    }//user test
 
    //exit
    else 
        return 0;
   	 
}//end main
