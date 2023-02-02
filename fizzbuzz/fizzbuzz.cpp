/*
  * WRITTEN BY JACKIE HENSON, 2020
  * Written in C++
  *
  * fizzbuzz - a program that runs the classic game "fizbuzz"
  * which will print "fizz" on multiples of three and "buzz" on multiples of five
  * as well as "fizzbuzz" on multiples of both
  * to run on a linux env, type
  * g++ fizzbuzz.cpp; ./a.out
  */

#include <iostream>
#include <string>

using namespace std; //for simplicities sake

/*
 * fizzbuzz - when called, will print the game of fizzbuzz
 * arugments: numIterations, the number of iterations provided
 * TIME COMPLEXITY - O(n)
 */
void fizzbuzz(int numIterations){
  for(int i = 0; i < numIterations; i++){
    if(i%3 == 0){ cout << "fizz"; }
    if(i%5 == 0){ cout << "buzz"; }
    else if (i%3 != 0 && i%5 != 0){
      cout << i;
    }
    cout << endl;
  }
}

/*
* main
*/
int main(){
  fizzbuzz(100);
  exit(0);
}
