/*
  * WRITTEN BY JACKIE HENSON, 2023
  * Written in C#
  *
  * Palindrome number - 
  * If given an integer, it'll return true if the number is a palindrome, otherwise false
  */

    public bool IsPalindrome(int x) {
        string xstring =  x.ToString(); 
        int half_length = xstring.Length / 2; //should round to the nearest proper value  
        
        for(int i=0; i < half_length; i++)   //loop thru the entire half-string
        {
            if(xstring[i] != xstring[xstring.Length-1-i]) //If any character is not the same, return false
                return false;
        }
        //If we haven't returned false already, return true by default here  
        return true;                    
    }

//Time complexity is linear here, so O(n), where n is the number of chars in the string