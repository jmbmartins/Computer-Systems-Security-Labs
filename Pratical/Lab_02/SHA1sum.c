#include <openssl/sha.h>
#include <stdio.h>

int main(int argc, char *argv[]){
   SHA_CTX sha1_ctx;
   SHA1_Init(&sha1_ctx);
   unsigned char caMD[20];
   unsigned char caByte[4];
   unsigned long lRand = atoi(argv[1]);

   caByte[3]= lRand & 0xff;
   caByte[2]= (lRand>>8) & 0xff;
   caByte[1]= (lRand>>16) & 0xff;
   caByte[0]= (lRand>>24) & 0xff;
   SHA1_Update(&sha1_ctx,&caByte,4);

   SHA1_Final(caMD,&sha1_ctx);
   int i;
   for(i = 0; i < 20; i++)
     printf("%02x",caMD[i] );
   printf("\n");
}
