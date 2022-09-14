from array import array
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WatchMovieRequestModel(BaseModel):
    numMovies: int
    qtyMoviesToWatch: int
    listMoviesToWatch: list
    
# Get current movie stack
@app.get("/")
def getCurrentMovieStack():
    currentMoviesStack = readMoviesStackFromFile()
    return currentMoviesStack

@app.post("/")
async def watchMovies(watchMovieRequestModel: WatchMovieRequestModel):
    currentMoviesStack = readMoviesStackFromFile()
    result = run(currentMoviesStack, 
               watchMovieRequestModel.numMovies, 
               watchMovieRequestModel.qtyMoviesToWatch,
               watchMovieRequestModel.listMoviesToWatch);
    saveMoviesStackToFile(result[1])
    return result

def saveMoviesStackToFile(moviesStack):
    with open('moviesStack.txt', 'w') as fp:
        for movie in moviesStack:
            fp.write("%s\n" % movie)
        
def readMoviesStackFromFile():
    movies = []
    with open('moviesStack.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current line
            x = line[:-1]
            movies.append(int(x))
    return movies

def run(moviesStack, n, m, movies):
    if n < 1 or m > 100000 or m < 1 or len(movies) < 1: return None
    movies_array = None
    if len(moviesStack) < 1:
        moviesStack = list(range(1, n+1))
    print(moviesStack)

    locations = {}
    for i in range(0, len(moviesStack)):
        locations[moviesStack[i]] = i
    
    # Watch movies
    for i in range(0, len(movies)):
        posOfTheMovie = locations[movies[i]]
        if movies_array == None:
            movies_array = str(posOfTheMovie)
        else:
                movies_array += ',' + str(posOfTheMovie)
        for pos in reversed(range(posOfTheMovie+1)):
            if pos > 0:
                moviesStack[pos]= moviesStack[pos-1]
                # Update locations
                locations[moviesStack[pos]] += 1
        moviesStack[0] = movies[i]
        locations[movies[i]] = 0
    #saveMoviesStackToFile(moviesStack) # Save movie stack to a file
    return [movies_array, moviesStack]

