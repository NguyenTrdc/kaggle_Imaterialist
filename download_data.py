import json
import os
import requests
from selenium import webdriver


os.makedirs("data", exist_ok=True)


def download_data(file,folder):

    folder_path = f"data/{folder}"
    timeout_seconds = 10  # Specify the maximum allowed execution time in seconds

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Open the JSON file
    with open(f'imaterialist-challenge-furniture-2018/{file}.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)
        data = data["images"]

    # Download the data
    i = 0
    for img in data :
        print(i)
        try:
            img_url = img["url"][0]
            filename = f"{str(img['image_id'])}.jpg" # Filename is the image id

            response = requests.get(img_url,timeout=timeout_seconds) # Send a GET request to the URL

            # Check if the request was successful
            if response.status_code == 200:
                # Open a file in binary write mode within the specified folder
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'wb') as file:
                    # Write the response content (image data) to the file
                    file.write(response.content)
                print('Image downloaded successfully.')
            else:
                print('Failed to download image. Status code:', response.status_code)

        except requests.Timeout:
            print('Download timeout exceeded. Skipping file download.')

        except Exception as e :
            print('Error occurred while downloading the image:', str(e))
            print('Skipping file download.')

        i+=1

# Downloading from json files, test, train and validation data
download_data("test","test_img")
download_data("train","train_img")
download_data("validation","validation_img")
