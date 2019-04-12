#%%
!pip install azure-cognitiveservices-vision-customvision
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"

# Replace with a valid keys
training_key = "<<Insert Training Key>>"
prediction_key = "<<Insert Predication Key>>"
projectid ="<<Insert Project ID>>"
iterationid="<<Insert Iteration ID>>"

#%%
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# Now there is a trained endpoint that can be used to make a prediction

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

test_img_url ="https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3051392.png"
results = predictor.predict_image_url(projectid, iterationid, url=test_img_url)

# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))