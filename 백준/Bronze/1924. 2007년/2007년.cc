#include <stdio.h>

int main()
{
	int x, y;
	int temp = 0;
	scanf("%d %d", &x, &y);

	int month[13];
	month[1] = month[7] = month[3] = month[5] = month[8] = month[10] = month[12] = 31;
	month[4] = month[6] = month[9] = month[11] = 30;
	month[2] = 28;
	month[0] = 0;
	for (int i = 0; i < x-1; i++) {
		temp += month[i+1];
	}
	temp += y;
	//printf("%d\n", temp);
	int nal = temp % 7;
	switch (nal)
	{
	case 0:
		printf("SUN");
		break;
	case 1:
		printf("MON");
		break;
	case 2:
		printf("TUE");
		break;
	case 3:
		printf("WED");
		break;
	case 4:
		printf("THU");
		break;
	case 5:
		printf("FRI");
		break;
	case 6:
		printf("SAT");
		break;
	}

}