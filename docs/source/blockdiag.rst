.. blockdiag::

  diagram {
 
   Chromosomes [stacked];
   "MPI enabled" [shape = diamond];
   MGEScan [shape = roundedbox];
   nonLTR -> "Protein Translation by bioperl" -> "Signals of APE by hmmer" -> 'E-values from 12 clades by hmmer' -> 'Searching path of  
   states' -> 'classification by hmmer (post processing)';
   "Signals of APE by hmmer" -> 'E-values from 12 clades by hmmer' [folded];
   LTR -> "TRF" -> "Finding pairs of maximal exact  repeats by modified GAME" -> 'Identifying putative LTRs - emboss matcher to find 
   similarity' -> 'analysis of RT domains / Scanning ORFs by hmmer, emboss transeq' -> 'Deleting fragments';
   "Finding pairs of maximal exact  repeats by modified GAME" -> 'Identifying putative LTRs - emboss matcher to find similarity' [folded]    ;
   }
