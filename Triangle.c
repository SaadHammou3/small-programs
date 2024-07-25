// Program that draws a triangle with a user-defined number of rows.

#include <stdio.h>

int main()
{
	int row, spaceNum, asterNum, rowNum, i, j;
	printf("Enter number of desired rows: ");
	scanf("%d", &rowNum);
	spaceNum = rowNum;
	asterNum = 1;
	for (row = 0; row < rowNum; row++)
	{
		for (i = 0; i < spaceNum; i++)
		{
			printf(" ");
		}
		for (j = 0; j < asterNum; j++)
		{
			printf("*");
		}
		printf("\n");
		spaceNum -= 1;
		asterNum += 2;
	}
	return 0;
}
