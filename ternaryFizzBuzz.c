// An attempt to implement a FizzBuzz algorithm in one line
// Saad Hammou, 23/11/2020

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i = 0;
	char convertedInt[3];
	char *output;

	for (i = 0; i < 101; i++)
	{
		sprintf(convertedInt, "%d", i);
		output = (i % 3 == 0 && i % 5 == 0) ? "FizzBuzz" : ( (i % 3 == 0) ? "Fizz" : (i % 5 == 0) ? "Buzz" : convertedInt ); 
		
		printf("%s\n", output);	
	}

	return 0;
}
