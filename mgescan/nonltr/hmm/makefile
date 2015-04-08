CC =	gcc
CFLAGS = -O3 -Wall -w
SRCS =	util_lib.c hmm_lib.c test_hmm.c
OBJS = $(SRCS:.c=.o) -lm
MAIN = MGEScan

$(MAIN): $(OBJS) 
	$(CC) $(CFLAGS) -o $(MAIN) $(OBJS)

.c.o:
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) *.o *~ $(MAIN)

# DO NOT DELETE
