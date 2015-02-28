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
	struct dirent *ent;
	char *flist = (char *)malloc(sizeof(char) * FILE_MAX * NAME_MAX);
	assert(flist != NULL);
	int nfiles = 0;

	if ((dir = opendir (path)) != NULL) {
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

	int i;
	if(flist){  
		for( i = 0 ; i < nfiles ; i++ ){
			if (strcmp(flist + (NAME_MAX * i),"") != 0 )
				printf ("[%d:%d]%s\n", world_rank, i, (flist + (NAME_MAX * i)));//, filename[i]);
		}}
}

void run_system_command(char *flist, int world_rank, int nfiles) {

	int i;
	int res;
	char tmp[1024];
	//MPI_Comm everyone;           /* intercommunicator */ 
	if(flist){
		for( i = 0 ; i < nfiles ; i++ ){
			if (strcmp(flist + (NAME_MAX * i) , "") != 0 ) {
				//MPI_Comm_spawn("ls", argv, 1, MPI_INFO_NULL, 0, MPI_COMM_WORLD, &everyone, MPI_ERRCODES_IGNORE);
				//res= system(tmp);
				sprintf(tmp, "hmmsearch --tblout tbl1 --noali -E 0.000001 /home/mpiuser/mgescan/CR1.en.hmm3 /home/mpiuser/mgescan/Drosophila_melanogaster.BDGP5.dna.chromosome.2L.fa");
				printf("%s\n",tmp);
				res = system(tmp);
				printf ("%d", res);
				fflush(stdout);
			}}}
}

int main(int argc, char** argv) {
  
	int world_rank;
	int world_size;
	char *flist;
	int nfiles = 0;
	int per_node = 1;
	int* nfiles_copy = (int*)malloc(sizeof(int));

	MPI_Init(NULL, NULL);
	MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
	MPI_Comm_size(MPI_COMM_WORLD, &world_size);

	assert(nfiles_copy != NULL);

	/* Root */
	if (world_rank == 0) {
		_readdir("./", &flist, &nfiles);
		*nfiles_copy = nfiles;
		//list_filenames(flist, world_rank, nfiles);
	}
	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Bcast(nfiles_copy, 1, MPI_INT, 0, MPI_COMM_WORLD);
	per_node = NAME_MAX * (*nfiles_copy / world_size + 1);
	char *sub_results = (char *)malloc(sizeof(char) * per_node);
	assert(sub_results != NULL);
	MPI_Scatter(flist, per_node , MPI_CHAR, sub_results,
			per_node, MPI_CHAR, 0, MPI_COMM_WORLD);
	list_filenames(sub_results, world_rank, per_node / NAME_MAX);
	//MPI_Gather(&sub_avg, 1, MPI_FLOAT, sub_avgs, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

	// Clean up
	if (world_rank == 0) 
		free(flist);
	free(sub_results);

	MPI_Barrier(MPI_COMM_WORLD);
	MPI_Finalize();

	return 0;
}
