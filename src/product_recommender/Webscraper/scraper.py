import os
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
import json

def run_scraper():
    # Open the JSON file
    with open(r"keyword.json") as f:
        products = json.load(f)

    # Configure WebDriver
    driver_path = r"C:\Users\User\Downloads\chrome-win64\chrome-win64"  # Replace with the actual path to the downloaded driver

    # Launch Browser and Open the URL
    for item, url in products.items():
        item_folder = os.path.join(r"C:\Users\User\Desktop\Blessing_AI\AI-ML\MKD-DS-Coding-TASK\Artifacts\scraped_images", item)
        os.makedirs(item_folder, exist_ok=True)  # Create folder for each item if it doesn't exist
        counter = 0

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = uc.Chrome(options=options)

        driver.get(url)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(4)

        img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

        image_urls = []
        for img in img_results:
            image_urls.append(img.get_attribute('src'))

        modifiedName = item.replace("+", " ")

        for i, img_url in enumerate(image_urls):
            counter += 1
            try:
                # Create item folder if it doesn't exist
                os.makedirs(item_folder, exist_ok=True) 
                urllib.request.urlretrieve(str(img_url), os.path.join(item_folder, "{} {}.jpg".format(modifiedName, counter)))
            except Exception as e:
                print("Error downloading image {}: {}".format(counter, e))
            
            if counter == 150:
                break  # Stop scraping when 300 images are downloaded

        driver.quit()


