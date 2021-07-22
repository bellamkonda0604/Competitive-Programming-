// Write the method vowelCount(s), that takes a string s, 
// and returns the number of vowels in s, ignoring case, 
// so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).


public class MyString {
	public int vowelCount(String s){
		// Your code goes here...
		int count = 0;
		for(int i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
			if (ch == 'A' || ch == 'a' || ch == 'E' || ch == 'e' || ch == 'I' || ch == 'i' || ch == 'O' || ch == 'o' || ch == 'U' || ch == 'u'){
				count = count + 1;
			}
		}
		return count;
	}
	
}