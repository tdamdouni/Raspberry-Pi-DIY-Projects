#include <stdio.h>
#include <stdlib.h>
int main(void)
{
char *data;
int dataLen;
long m,n;

printf("%s%c%c\n",
"Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<TITLE>Multiplication results</TITLE>\n");
printf("<H3>Multiplication results</H3>\n");

printf("<p>Query_string = ");  // look at what the query_strin is.
printf(getenv("QUERY_STRING"));

dataLen = atoi(getenv("CONTENT_LENGTH")); // Get the length of the data send by index.html
					  // Also convert it to an int.
printf("<p>Contec_length = "); // Show the length of the query.
printf("%d", dataLen);

data = malloc(dataLen); // Alocate the amount of data needed for the query.
fread(data, dataLen, 1, stdin); // Read the query form stdin (from the form post).

printf("<p>data = "); // Show the query.
printf(data);

if(data == NULL)
  printf("<P>Error! Error in passing data from form to script.");
else if(sscanf(data,"m=%ld&n=%ld",&m,&n)!=2) // Check if the query contains the right data.
  printf("<P>Error! Invalid data. Data must be numeric.");
else
  printf("<P>The product of %ld and %ld is %ld.",m,n,m*n); // Show the calculation.

free(data);

return 0;
}
