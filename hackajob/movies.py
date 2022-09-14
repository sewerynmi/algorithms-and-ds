 
class Solution:
    
    def run(self, n, m, movies):
        movies_array = None
        maxMovieLabel = max(movies) # Get max label of movie to watch to reduce movies list size
        moviesList = list(range(1,maxMovieLabel+1)) # Fill in list with movies labels from 1 to maxMovieLabel
        # Initial location of movies to watch
        locations = {}
        for i in range(0, len(movies)):
            locations[movies[i]] = movies[i] - 1
        
        # Watching movie
        for i in range(0, len(movies)):
            #print("I am watching movie :", movies[i]) # Remove line in prod
            watchedMovie = movies[i]
            ## Record how many movies was ahead of the movie [check locations dictionary]
            posOfTheMovie = locations[watchedMovie]
            #print('position of the movie is: ', posOfTheMovie) # Remove line in prod
            if movies_array == None:
                movies_array = str(posOfTheMovie)
            else:
                 movies_array += ',' + str(posOfTheMovie)
            
            ## Move movie to the top of the stack and move all other items [update also locations dict.]
            #print("Movie list before: " , moviesList)
            ## UPDATE MOVIES INDEXES
            moviesList = [moviesList[posOfTheMovie]] + moviesList[:-1]
            #print("Movie list now: " , moviesList)
            ## Update indexes in locations
            #print('locations before: ', locations);
            for j in range(0, posOfTheMovie):
                ## Update locations indexes
                if moviesList[j] in locations:
                    locations[moviesList[j]] += 1
            
            locations[watchedMovie] = 0
        
        
        return movies_array

# if __name__ == "__main__":
#     solution = Solution()
#     test1 = solution.run(3, 3, [3,1,1])
#     print('\ntest1 expected : 2,1,0')
#     print('test1 actual   : ' , test1)
#     print('PASS\n') if test1 == "2,1,0" else print("FAIL\n") 

    
#     test2 = solution.run(5,3, [4,4,5])
#     print('\ntest2 expected : 3,0,4')
#     print('test2 actual   :' , test2)
#     print('PASS\n') if test2 == "3,0,4" else print("FAIL\n") 

import unittest

class SolutionMethods(unittest.TestCase):
   
    def test_ONE(self):
        solution = Solution()
        self.assertEqual(solution.run(3,3, [3,1,1]), "2,1,0")
  
    def test_TWO(self):
        solution = Solution()
        self.assertEqual(solution.run(5,3, [4,4,5]), "3,0,4")


if __name__ == "__main__":
	unittest.main()