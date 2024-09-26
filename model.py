import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "cd0ee3b0-7a42-11ef-8eca-f73d5ad594e13bbab265-1a28-4cde-bfb9-a293be8fc302"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def myModel(text):
    # CHANGE THIS to something you want your machine learning model to classify
    demo = classify(text)

    label = demo["class_name"]
    confidence = demo["confidence"]

    return label, confidence