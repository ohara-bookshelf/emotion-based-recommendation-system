from fastapi import FastAPI
from pydantic import BaseModel

# from model.model import get_top_genres, recommend
# from model.model import __version__ as model_version

from app.model.model import get_top_genres, recommend
from app.model.model import __version__ as model_version

# import uvicorn
#import traceback


app = FastAPI(title="Ohara-Bookshelf Model API", version="2.0.0", description="This is a simple API for the Bookshelf recommendation system according to user emotion ML Model")



class EmotionInput(BaseModel):
    text: str

class RecommendationCountInput(BaseModel):
    count: int

class RecommendationOutput(BaseModel):
   #The recommentation output will be a list of book ISBNs
    books: list

class TopGenresCountInput(BaseModel):
    count: int

class TopGenresOutput(BaseModel):
    genres: list


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}



@app.post("/top_genres", response_model = TopGenresOutput)
def top_genres(emotion:EmotionInput, count: TopGenresCountInput):
    #Get the top genres for the given emotion
    top_genres = get_top_genres(emotion.text, count.count)
    #Return the list
    return {"genres": top_genres}


@app.post("/emotion-based-recommend", response_model = RecommendationOutput)
def emotion_based_recommend(emotion:EmotionInput, count: RecommendationCountInput):
    #Get the recommended books for the given emotion
    recommended_books = recommend(emotion.text, count.count)
    #Return the list
    return {"books": recommended_books}




# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=4000)

