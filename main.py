import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from models import Movie

app = FastAPI(debug=True)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


movies_db = {}


@app.get("/all_movies/")
def get_all_movies():
    return {"all": movies_db}


@app.post("/new_movie/")
def add_movie(movie: Movie):
    if movie.id in movies_db:
        raise HTTPException(status_code=400, detail="Фільм з таким ID вже існує")
    movie_id = len(movies_db)
    movies_db[movie_id] = movie
    return movie


@app.get("/movies/{id}")
def get_movie(id: int):
    if id in movies_db:
        return movies_db[id]
    raise HTTPException(status_code=404, detail="Фільм не знайдено")


@app.delete("/movies/{id}")
def delete_movie(id: int):
    if id in movies_db:
        del movies_db[id]
        return {"сonclusion": "Фільм успішно видалено"}
    raise HTTPException(status_code=404, detail="Фільм не знайдено")


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
