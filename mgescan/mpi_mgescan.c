#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <mpi.h>
#include <assert.h>
#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>

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

void run_system_command(char *flist, char *cmd, char **params, char *data_path, int world_rank, int nfiles) {

	//MPI_Comm everyone;           /* intercommunicator */ 
	if(flist){
		int i;
		int res;
		char tmp[BUFSIZ];
		char *params_all = (char *)malloc(sizeof(char) * BUFSIZ);
		strcpy(params_all, "");
		for (i = 0; params[i] ; i++) {
			strcat(params_all, params[i]);
			strcat(params_all, " ");
		}
		for( i = 0 ; i < nfiles ; i++ ){
			if (strcmp(flist + (NAME_MAX * i) , "") != 0 ) {
				//MPI_Comm_spawn("ls", argv, 1, MPI_INFO_NULL, 0, MPI_COMM_WORLD, &everyone, MPI_ERRCODES_IGNORE);
				//res= system(tmp);
				sprintf(tmp, "%s %s %s/%s", cmd, params_all, data_path, flist + (NAME_MAX * i));
				printf("%s\n",tmp);
				res = system(tmp);
				//printf ("%d", res);
				fflush(stdout);
			}}}
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

int main(int argc, char** argv) {
  
	if (argc != 3) {
		fprintf(stderr, "Usage: %s DATA_DIR COMMAND\n", argv[0]);
		exit(1);
	}
	char *data_path = argv[1];
	char **tokens = str_split(argv[2], ' ');
	char *cmd = tokens[0];
	char **params = tokens + 1;

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
		_readdir(data_path, &flist, &nfiles);
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
	run_system_command(sub_results, cmd, params, data_path, world_rank, num_per_node);
	//MPI_Gather(&sub_avg, 1, MPI_FLOAT, sub_avgs, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

	// Clean up
	if (world_rank == 0) 
		free(flist);
	free(sub_results);

	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Finalize();

	return 0;
}
