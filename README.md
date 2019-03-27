[![Build Status](https://travis-ci.org/orionoiro/path_searcher.svg?branch=master)](https://travis-ci.org/orionoiro/path_searcher)

  Using a data from map in .txt file. For example: 
  
    32 76 54 23 = From To TotalDistance DistanceOutdoors. 
      This entry would become an edge from 32 to 76.
  
  Path_searcher solves a simple optimization problem on a graph. 
  It finds the shortest route from one building to another using depth-first search algorithm.
