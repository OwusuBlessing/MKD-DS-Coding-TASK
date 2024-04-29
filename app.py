from flask import Flask, render_template, request,redirect
from src.product_recommender.endpoints.natural_query import query,llm_response
from src.product_recommender.OCR.extract_text import extract_text
from src.product_recommender.image_recognition.predict import data_transform,load_tinyvgg_model,predict
import os

app = Flask(__name__)

# Define routes and functions here

@app.template_filter()
def my_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    input_text = request.form['input_text']
    
    # Process the input text and generate result (a list)
    result =  llm_response(query(input_text))
    return render_template('home.html',result=result)


@app.route('/upload_image_ocr')
def upload_image():
    return render_template('upload_image_ocr.html')

UPLOAD_FOLDER = 'uploads'

@app.route('/process_image_ocr', methods=['POST'])
def process_image():
    
    # Get the uploaded file
    uploaded_file = request.files['image_file']
    
    # Save the uploaded file to the server
    if uploaded_file:
        # Create the upload folder if it doesn't exist
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        filename = uploaded_file.filename
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        uploaded_file.save(image_path)

        if os.path.exists(image_path):

            processed_text = extract_text(img_path=image_path) #extract text wit ocr
            result =  llm_response(query(processed_text)) #pass text to recommnder engine
            # Render the upload_image.html template with the result and image path
           
            return render_template('upload_image_ocr.html',result=result, image_path=image_path)
    else:
        # If no file was uploaded, redirect back to the upload page
        return redirect('/upload_image_ocr')


@app.route('/upload_image_cnn')
def upload_image_cn():
    return render_template('upload_image_cnn.html')

UPLOAD_FOLDER_CNN = 'uploads_cnn'
@app.route('/process_image_cnn', methods=['POST'])
def process_image_cn():
    
    # Get the uploaded file
    uploaded_file = request.files['image_file']
    
    # Save the uploaded file to the server
    if uploaded_file:
        # Create the upload folder if it doesn't exist
        if not os.path.exists(UPLOAD_FOLDER_CNN):
            os.makedirs(UPLOAD_FOLDER_CNN)
        
        filename = uploaded_file.filename
        image_path = os.path.join(UPLOAD_FOLDER_CNN, filename)
        uploaded_file.save(image_path)

        if os.path.exists(image_path):

            loaded_model = load_tinyvgg_model(input_shape=3,
                                  model_save_path="Artifacts/trained_models/tinyvgg_model_1.pth",
                                  hidden_units=10,
                                  output_shape=3,
                                  device ="cpu"
)
            #predict label from image
            name,label = predict(model=loaded_model,image_path=image_path,
                        transform = data_transform)

            
            result =  llm_response(query(name)) #pass text to recommnder engine
            # Render the upload_image.html template with the result and image path
           
            return render_template('upload_image_cnn.html',result=result, image_path=image_path)
    else:
        # If no file was uploaded, redirect back to the upload page
        return redirect('/upload_image_cnn')


if __name__ == '__main__':
    app.run(debug=True)



