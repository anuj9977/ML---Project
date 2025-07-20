# from flask import Flask,render_template,request
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import CustomData,PredictPipeline

# application = Flask(__name__)
# app=application

# # Define the home route
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route("/predictdata", methods=["GET", "POST"])
# def predict_datapoint():
#     if request.method == "POST":
#         try:
#             # Validate and convert form data to CustomData object
#             data = CustomData(
#                 gender=request.form.get("gender"),
#                 race_ethnicity=request.form.get("race ethnicity"),
#                 parental_level_of_education=(request.form.get("parental level of education")),
#                 lunch=(request.form.get("lunch")),
#                 test_preparation_course=(request.form.get("test preparation course")),
#                 reading_score=request.form.get("reading score"),
#                 writing_score=request.form.get("writing score"),
                
#             )

#             final_data = data.get_data_as_dataframe()
#             # Make prediction
#             predict_pipeline = PredictPipeline()
#             result = predict_pipeline.predict(final_data)
            
#             return render_template("home.html", results=result[0])

#         except Exception as e:
#             # Handle exceptions gracefully
#             error_message = f"Error during prediction: {str(e)}"
#             return render_template("error.html", error_message=error_message)

#     else:
#         # Render the initial page
#         return render_template("home.html")

# # Execution begins
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", debug=True)


from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        try:
            data = CustomData(
                gender=request.form.get("gender"),
                race_ethnicity=request.form.get("race_ethnicity"),
                parental_level_of_education=request.form.get("parental_level_of_education"),
                lunch=request.form.get("lunch"),
                test_preparation_course=request.form.get("test_preparation_course"),
                reading_score=int(request.form.get("reading_score")),
                writing_score=int(request.form.get("writing_score"))
            )
            final_df = data.get_data_as_dataframe()

            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(final_df)

            return render_template("home.html", results=result[0])

        except Exception as e:
            error_message = f"Error during prediction: {str(e)}"
            return render_template("error.html", error_message=error_message)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
