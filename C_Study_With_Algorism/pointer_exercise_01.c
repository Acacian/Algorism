#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void ChangeDouble(int* p) { /*int*p=&num;*/
    *p = *p * 2; 
}
int main()
{
    int num;
    printf("숫자를 입력하시오 : ");
    scanf_s("%d", &num); /*&num은 num의 변수 주소*/
    ChangeDouble(&num);
    printf("%d\n", num);
    return 0;
}