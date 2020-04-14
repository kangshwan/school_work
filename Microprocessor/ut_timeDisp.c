#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <signal.h>

#define THREAD_NUM 1

//Task function prototypes. 
static void *disp_time( void *arg ) {
    time_t rawt;
    struct tm *t;
	while(1){
	    time(&rawt);
	    t = localtime(&rawt);
	    printf("Time: %02d:%02d:%02d", t->tm_hour, t->tm_min, t->tm_sec);
    	fflush(stdout);
		sleep(1);
		printf("\r");
	}
}
//----------------------------------------------------------
int main( void )
{
    char c;
	pthread_t time_process;
	int status;
    printf("Seunghwan Kang 201600055\n");
    printf("Press any key and Enter to quit the program.... \n");
    fflush(stdout);
	pthread_create( &time_process, NULL, disp_time, NULL);
    scanf("%c", &c);
    fflush(stdout);
    printf("Bye~\n");
    return 0;
}

