#include <stdio.h>

int strncmp(char a[], char b[], int c)
{
	int i;

	for (i = 0; i < c; i++)
	{
		if (a[i] != b[i]) return 1;
	}
	return 0;
}

int exam_07()
{
	char a[] = "JAINA", b[] = "JAINE";
	int n = 0;

	n = strncmp(a, b, 4);

	printf("%d\n", n);

	if (n == 1)
		printf("�� ���ڿ��� �ٸ��ϴ�\n");
	else if (n == 0)
		printf("�� ���ڿ��� �����ϴ�\n");

}