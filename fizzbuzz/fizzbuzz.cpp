/*
  * WRITTEN BY JAKE HENSON
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
 * fizzbuzz - when called, will run number of iterations provided
 */
void fizzbuzz(int niters){
  for(int i = 0; i < niters; i++){
    if(i%3 == 0){ cout << "fizz"; }
    if(i%5 == 0){ cout << "buzz"; }
    else if (i%3 != 0 && i%5 != 0){
      cout << i;
    }
    cout << endl;
  }
}

int main(){
  fizzbuzz(100);
  exit(0);
}
