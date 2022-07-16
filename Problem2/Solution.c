#include <stdio.h>
#include <stdlib.h>

const int SIZE = 4000000;
int sequence[SIZE];

int main()
{
    sequence[0] = 1;
    sequence[1] = 1;
    int sum = 0;
    for (int i = 0; i < SIZE; i++)
    {
        if (sequence[i - 1] + sequence[i - 2] % 2 == 0)
        {
            sequence[i] = sequence[i - 1] + sequence[i - 2];
        }
    }
    for (int j = 0; j < SIZE; j++)
    {
        sum += sequence[j];
    }

    printf("%d", sum);
    return 0;
}
