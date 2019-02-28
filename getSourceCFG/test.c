#include <stdio.h>

int main(int argc, char const *argv[])
{
  int a = 1;
  int b = 2;
  int c;
  int count = 3;
  while (count > 0)
  {
    if (a > b)
    {
      c = a + b;
      printf("c1 = %d\n", c);
    }
    else
    {
      c = a - b;
      printf("c2 = %d\n", c);
    }
    --count;
  }
  return 0;
}
