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

void _readdir(const char *path, char **filenames, int *numbers) {
	DIR *dir;
	struct dirent *ent;

	char *files = (char *)malloc(sizeof(char) * FILE_MAX * NAME_MAX);
	int number_of_files = 0;

	if ((dir = opendir (path)) != NULL) {
		while ((ent = readdir (dir)) != NULL) {
			if (strcmp(ent->d_name, ".") == 0 || (strcmp(ent->d_name, "..") == 0) || ent->d_type != 0x8)
				continue;
			strcpy(files + (NAME_MAX * number_of_files), ent->d_name);
			number_of_files++;
			/*
			if (number_of_files > FILE_MAX) {
				files = (char *)realloc(files, sizeof(char) * number_of_files * 2);
			}*/
		}
		closedir (dir);
		*filenames = files;
		*numbers = number_of_files;
	}
} 

void listing_filenames(char *filename, int world_rank, int num) {
  int i =0;
  char **argv;
  //MPI_Comm everyone;           /* intercommunicator */ 

  if(filename){
  argv=(char **)malloc(3 * sizeof(char *)); 
  for(i=0;i<num;i++){
  if (strcmp(filename + (NAME_MAX * i),"") != 0 ) {
  //printf ("[%d:%d]%s\n", world_rank, i, (filename + (NAME_MAX * i)));//, filename[i]);
  //printf ("hmmsearch %s\n", (filename + (NAME_MAX * i)));//, filename[i]);
  argv[0] = "-al";
  argv[1] = (filename + (NAME_MAX * i));
  argv[2] = NULL;
  //MPI_Comm_spawn("ls", argv, 1, MPI_INFO_NULL, 0, MPI_COMM_WORLD, &everyone, MPI_ERRCODES_IGNORE);
  int res;
  char tmp[1000];
  // sprintf(tmp, "ls -al %s", (filename + (NAME_MAX * i)));
  //res= system(tmp);
  if (world_rank) {
  sprintf(tmp, "hmmsearch --tblout tbl1 --noali -E 0.000001 /home/mpiuser/mgescan/CR1.en.hmm3 /home/mpiuser/mgescan/Drosophila_melanogaster.BDGP5.dna.chromosome.2L.fa");
  printf("%s\n",tmp);
  }else {
  sprintf(tmp, "hmmsearch --tblout tbl2 --noali -E 0.000001 /home/mpiuser/mgescan/CR1.en.hmm3 /home/mpiuser/mgescan/Drosophila_melanogaster.BDGP5.dna.chromosome.2R.fa");
  printf("%s\n",tmp);
}
   res = system(tmp);

  printf ("%d", res);
      fflush(stdout);
  }
  }}
}

int main(int argc, char** argv) {

  MPI_Init(NULL, NULL);

  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  char *files;
  int numbers = 16;
  int per_node;
  int* data = (int*)malloc(sizeof(int));
  assert(data != NULL);
  if (world_rank == 0) {
    _readdir("./", &files, &numbers);
  *data = numbers;
    //listing_filenames(files, world_rank, numbers);
  }
  MPI_Barrier(MPI_COMM_WORLD);
  MPI_Bcast(data, 1, MPI_INT, 0, MPI_COMM_WORLD);
  per_node = NAME_MAX * (*data / world_size + 1);
  //printf ("[%d]%d,%d\n", world_size, *data, (*data/world_size+1));
  char *sub_results = (char *)malloc(sizeof(char) * per_node);// * NAME_MAX * numbers);
  MPI_Scatter(files, per_node , MPI_CHAR, sub_results,
              per_node, MPI_CHAR, 0, MPI_COMM_WORLD);
  listing_filenames(sub_results, world_rank, per_node/NAME_MAX);
  //listing_filenames(sub_results, world_rank, 1);
  // Gather all partial averages down to the root process
  if (world_rank == 0) {
  }
  //MPI_Gather(&sub_avg, 1, MPI_FLOAT, sub_avgs, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

  
  // Now that we have all of the partial averages on the root, compute the
  // total average of all numbers. Since we are assuming each process computed
  // an average across an equal amount of elements, this computation will
  // produce the correct answer.
  if (world_rank == 0) {
    //listing_filenames(sub_avgs, world_size);
    //printf("Avg of all elements is %f\n", avg);
  }

  // Clean up
  if (world_rank == 0) {
    free(files);
    //free(sub_avgs);
  }
  free(sub_results);
 
  MPI_Barrier(MPI_COMM_WORLD);
  MPI_Finalize();

  return 0;
}
