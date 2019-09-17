#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int nums = 0;
  char buff[BUFSIZ];
  fgets(buff,BUFSIZ,stdin);
  nums = atoi(buff);
  printf("%d",nums);
  fgets(buff, BUFSIZ, stdin);
  char *pbuf = &buff;
  while (*pbuf != '-'){
    pbuf++; 
  }
  printf("%c",*pbuf);
  return EXIT_SUCCESS;
}
