#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <mpi.h>
#include <assert.h>
#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>
#include <getopt.h>

#define NAME_MAX         255
#define FILE_MAX	 202747 // cat /proc/sys/fs/file-max

void _readdir(const char *path, char **flist_p, int *nfiles_p) {

	DIR *dir;
	if ((dir = opendir (path)) != NULL) {

		struct dirent *ent;
		char *flist = (char *)malloc(sizeof(char) * FILE_MAX * NAME_MAX);
		assert(flist != NULL);
		int nfiles = 0;

		while ((ent = readdir (dir)) != NULL) {
			if (strcmp(ent->d_name, ".") == 0 || (strcmp(ent->d_name, "..") == 0) || ent->d_type != 0x8)
				continue;
			strcpy(flist + (NAME_MAX * nfiles), ent->d_name);
			nfiles++;
			/*
			if (number_of_files > FILE_MAX) {
				files = (char *)realloc(files, sizeof(char) * number_of_files * 2);
			}*/
		}
		closedir (dir);
		*flist_p= flist;
		*nfiles_p = nfiles;
	}
} 

void list_filenames(char *flist, int world_rank, int nfiles) {

	if(flist){  
	int i;
		for( i = 0 ; i < nfiles ; i++ ){
			if (strcmp(flist + (NAME_MAX * i),"") != 0 )
				printf ("[%d:%d]%s\n", world_rank, i, (flist + (NAME_MAX * i)));//, filename[i]);
		}}
}

char** str_split(char* a_str, const char a_delim)
{
	char** result    = 0;
	size_t count     = 0;
	char* tmp        = a_str;
	char* last_comma = 0;
	char delim[2];
	delim[0] = a_delim;
	delim[1] = 0;

	/* Count how many elements will be extracted. */
	while (*tmp)
	{
		if (a_delim == *tmp)
		{
			count++;
			last_comma = tmp;
		}
		tmp++;
	}

	/* Add space for trailing token. */
	count += last_comma < (a_str + strlen(a_str) - 1);

	/* Add space for terminating null string so caller
	 *        knows where the list of returned strings ends. */
	count++;

	result = malloc(sizeof(char*) * count);

	if (result)
	{
		size_t idx  = 0;
		char* token = strtok(a_str, delim);

		while (token)
		{
			assert(idx < count);
			*(result + idx++) = strdup(token);
			token = strtok(0, delim);
		}
		assert(idx == count - 1);
		*(result + idx) = 0;
	}

	return result;
}

void echo_usage(char** argv) {
	fprintf(stderr, "Usage: %s -p ltr|nonltr -g GENOME_PATH -d OUTPUT_PATH -c COMMAND\n", argv[0]);
}

typedef struct arguments {
	char program[7];
	char genome[BUFSIZ];
	char data[BUFSIZ];
	int hmmerv;
	char cmd [BUFSIZ];
} ARGS;

void run_mgescan_cmd(char *flist, ARGS optarg, int nfiles) {

	//MPI_Comm everyone;           /* intercommunicator */ 
	if(flist){
		int i;
		int res;
		char tmp[BUFSIZ];
		char *params_all = (char *)malloc(sizeof(char) * BUFSIZ);
		strcpy(params_all, "");

		char **tokens = str_split(optarg.cmd, ' ');
		char *cmd = tokens[0];
		char **params = tokens + 1;

		for (i = 0; params[i] ; i++) {
			strcat(params_all, params[i]);
			strcat(params_all, " ");
		}
		for( i = 0 ; i < nfiles ; i++ ){
			if (strcmp(flist + (NAME_MAX * i) , "") != 0 ) {
				//MPI_Comm_spawn("ls", argv, 1, MPI_INFO_NULL, 0, MPI_COMM_WORLD, &everyone, MPI_ERRCODES_IGNORE);
				//res= system(tmp);
				sprintf(tmp, "%s %s %s/%s", cmd, params_all, optarg.data, flist + (NAME_MAX * i));
				printf("%s\n",tmp);
				res = system(tmp);
				//printf ("%d", res);
				fflush(stdout);
			}
		}
	}
}

ARGS arg_parse(int argc, char** argv) {

	int c;
	/* Flag set by ‘--verbose’. */
	static int verbose_flag;
	static struct option long_options[] =
	{
		{"prg",  required_argument, 0, 'p'},
		{"genome",  required_argument, 0, 'g'},
		{"data",    required_argument, 0, 'd'},
		{"hmmerv",    required_argument, 0, 'v'},
		{"cmd",    required_argument, 0, 'c'},
		{0, 0, 0, 0}
	};

	ARGS pargs = {0};
	pargs.hmmerv = 3; /* default HMMER 3.0 */

	/* getopt_long stores the option index here. */
	int option_index = 0;

	while((c = getopt_long (argc, argv, "p:g:d:v:c:",
			long_options, &option_index)) != -1) {
		switch (c)
		{

			case 'p':
				strcpy(pargs.program, optarg);
				break;

			case 'g':
				strcpy(pargs.genome, optarg);
				break;

			case 'd':
				strcpy(pargs.data, optarg);
				break;

			case 'v':
				pargs.hmmerv = atoi(optarg);
				break;

			case 'c':
				strcpy(pargs.cmd, optarg);
				break;

			case '?':
				/* getopt_long already printed an error message. */
				break;

			default:
				echo_usage(argv);
				return;
		}
	}
	return pargs;
}

int main(int argc, char** argv) {

	ARGS optarg = arg_parse(argc, argv);
	if (strcmp(optarg.program, "") == 0 ||
			strcmp(optarg.genome, "") == 0 ||
			strcmp(optarg.data, "") == 0 ||
			strcmp(optarg.cmd, "") == 0) {
		echo_usage(argv);
		return -1;
	}

	MPI_Init(NULL, NULL);

	int world_rank;
	MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
	int world_size;
	MPI_Comm_size(MPI_COMM_WORLD, &world_size);

	int* nfiles_copy = (int*)malloc(sizeof(int));
	assert(nfiles_copy != NULL);

	/* Root */
	char *flist;
	int nfiles = 0;
	if (world_rank == 0) {
		_readdir(optarg.genome, &flist, &nfiles);
		*nfiles_copy = nfiles;
		//list_filenames(flist, world_rank, nfiles);
	}

	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Bcast(nfiles_copy, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int num_per_node = *nfiles_copy / world_size + 1;
	int bytes_per_node = NAME_MAX;
	bytes_per_node *= num_per_node;
	char *sub_results = (char *)malloc(sizeof(char) * bytes_per_node);
	assert(sub_results != NULL);

	MPI_Scatter(flist, bytes_per_node , MPI_CHAR, sub_results,
			bytes_per_node, MPI_CHAR, 0, MPI_COMM_WORLD);
	run_mgescan_cmd(sub_results, optarg, num_per_node);
	//MPI_Gather(&sub_avg, 1, MPI_FLOAT, sub_avgs, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

	// Clean up
	if (world_rank == 0) 
		free(flist);
	free(sub_results);

	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Finalize();

	return 0;
}
