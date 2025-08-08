import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from IPython.display import display, clear_output
from PIL import Image, ImageFilter, ImageEnhance
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Data processing of dataset
def process_data(file_path, numerical_columns):  
    try: 
        df = pd.read_csv(file_path)
        
        print("Initial dataset preview:")
        print(df.head())
        
        print("Dataset info:")
        print(df.info())
        
        for col in numerical_columns:
            if df[col].isnull().any():
                print(f"Column '{col}' has missing values.")
                df[col].fillna(df[col].mean(), inplace=True)  
                
        for col in numerical_columns:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found in the dataset.")
                
        if df[numerical_columns].shape[0] == 0:
            raise ValueError("No data available after handling missing values.")
            
        scaler = StandardScaler()
        df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
        
        print("Data standardized. Example of processed data:")
        return df

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def run_data_processing():
    file_path = r"C:\Users\tannu\Desktop\people.csv"
    numerical_columns_input = input("Enter numerical columns to standardize, separated by commas (e.g., Age, Salary): ")
    numerical_columns = [col.strip() for col in numerical_columns_input.split(',')]
    processed_df = process_data(file_path, numerical_columns)
    if processed_df is not None and not processed_df.empty:
        display(processed_df.head())
    else:
        print("Processed DataFrame is empty.")

# Function to predict using the model
def predict(features):
    try:
        model = joblib.load('cricket_model.pkl')
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)
        return int(prediction[0])
    except Exception as e:
        print(f"Prediction error: {str(e)}")

# Capture image and detect/crop face
def capture_image():
    cam = cv2.VideoCapture(0) 
    cv2.namedWindow("Capture Image")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Capture Image", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            img_name = "captured_image.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved!")
            break

    cam.release()
    cv2.destroyAllWindows()
    return img_name

def crop_face(image_path):
    img = cv2.imread(image_path)
    faces, confidences = cv.detect_face(img)
    if faces:
        for face in faces:
            (startX, startY) = face[0], face[1]
            (endX, endY) = face[2], face[3]
            cropped_face = img[startY:endY, startX:endX]
            
            cv2.imshow("Cropped Face", cropped_face)
            cropped_face_path = "cropped_face.png"
            cv2.imwrite(cropped_face_path, cropped_face)
            print(f"Cropped face saved as {cropped_face_path}")
            
            img[startY:endY, startX:endX] = cropped_face
            cv2.imshow("Image with Cropped Face", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return cropped_face_path
    else:
        print("No face detected")
        return None

def run_face_detection():
    image_path = capture_image()
    if image_path:
        cropped_face_path = crop_face(image_path)

# Apply different filters on an image
def run_image_filtering():
    image_path = r"C:\Users\ASUSR\Desktop\Machine Learning\crown.png"
    image = Image.open(image_path)
    
    filters = [
        ("Blurred", ImageFilter.BLUR),
        ("Contour", ImageFilter.CONTOUR),
        ("Detail", ImageFilter.DETAIL),
        ("Sharpened", ImageFilter.SHARPEN),
        ("Edge Enhanced", ImageFilter.EDGE_ENHANCE),
        ("Embossed", ImageFilter.EMBOSS),
    ]
    
    for filter_name, filter_type in filters:
        filtered_image = image.filter(filter_type)
        filtered_image.show(title=filter_name)
        filtered_image.save(f"{filter_name.lower().replace(' ', '_')}_image.jpg")

    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.5)  
    bright_image.show()  

    enhancer = ImageEnhance.Contrast(image)
    contrast_image = enhancer.enhance(2.0)  
    contrast_image.show()  
    
    enhancer = ImageEnhance.Color(image)
    color_image = enhancer.enhance(1.5)  
    color_image.show()  
    
    gray_image = image.convert("L")
    gray_image.show()  

    bright_image.save("bright_image.jpg")
    contrast_image.save("contrast_image.jpg")
    color_image.save("color_image.jpg")
    gray_image.save("gray_image.jpg")

# Create a custom image using numpy
def run_custom_image_creation():
    width, height = 300, 300

    # Create a 3D NumPy array of shape (height, width, 3) for an RGB image
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            image_array[y, x] = [x % 256, y % 256, (x + y) % 256]
    image = Image.fromarray(image_array)
    image.show()
    image.save("custom_image.png")

# Apply sunglass and cap on an image
def run_cool_filter():
    image_path = r"C:\Users\ASUSR\Desktop\Machine Learning\crown.png\IMG_8820.jpg" 
    image = Image.open(image_path)

    sunglasses_path = r"C:\Users\ASUSR\Desktop\sunglass and cap\pngwing.com (1).png"
    cap_path = r"C:\Users\ASUSR\Desktop\sunglass and cap\pngwing.com (2).png"

    sunglasses = Image.open(sunglasses_path)
    cap = Image.open(cap_path)

    sunglasses = sunglasses.resize((300, 150))  
    cap = cap.resize((300, 150))  

    sunglasses_position = (500, 240) 
    image.paste(sunglasses, sunglasses_position, sunglasses)
    cap_position = (300, 250)  
    image.paste(cap, cap_position, cap)

    image.show()
    image.save("image_with_accessories.jpg")

# Menu to run the project tasks
def menu():
    while True:
        print("\nMachine Learning Project Menu")
        print("1. Automatic Data Processing")
        print("2. Predict Outcome")
        print("3. Face Detection and Cropping")
        print("4. Apply Filters to Image")
        print("5. Create Custom Image")
        print("6. Apply Cool Filters")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            run_data_processing()
        elif choice == '2':
            features_input = input("Enter features separated by commas: ")
            features = [float(f.strip()) for f in features_input.split(',')]
            prediction = predict(features)
            print(f"Prediction: {prediction}")
        elif choice == '3':
            run_face_detection()
        elif choice == '4':
            run_image_filtering()
        elif choice == '5':
            run_custom_image_creation()
        elif choice == '6':
            run_cool_filter()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
