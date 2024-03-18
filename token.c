#include <string.h>
#include <stdio.h>

/* /또는 - 또는 : 또는 space를 delimiter로 사용합니다. */

#define DELIM_CHARS     "/-: "

int main(int argc, char **argv)
{
    char time[1024] = "2017-02-12 10:25:30";
    char *ret_ptr;
    char *next_ptr;

    printf("time : [%s]\n", time);

    ret_ptr = strtok_r(time, DELIM_CHARS, &next_ptr);

    while(ret_ptr) {
        printf("ret_ptr = [%s]\n", ret_ptr);

        ret_ptr = strtok_r(NULL, DELIM_CHARS, &next_ptr);
    }

    return 0;
}

// 결과:
// time : [2017-02-12 10:25:30]
// ret_ptr = [2017]
// ret_ptr = [02]
// ret_ptr = [12]
// ret_ptr = [10]
// ret_ptr = [25]
// ret_ptr = [30]