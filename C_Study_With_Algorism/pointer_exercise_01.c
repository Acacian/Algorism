//int형 변수를 선언하여 사용자에게 입력받은 후 해당 값을 2배로 바꿔주는 함수(반환 형태 : void)를 사용하여 입력받은 수의 3배를 출력하시오

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void ChangeDouble(int* p) { /*int*p=&num;*/
    *p = *p * 3; 
}
int main()
{
    int num;
    printf("숫자를 입력하시오 : ");
    scanf("%d", &num); /*&num은 num의 변수 주소*/
    ChangeDouble(&num);
    printf("%d\n", num);
    return 0;
}