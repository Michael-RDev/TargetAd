# TargetAd - Personalized Advertising Recommendations

Welcome to TargetAd, your go-to solution for personalized advertising recommendations. TargetAd harnesses the power of demographic data, obtained through a webcam, to provide tailored ad suggestions, ensuring your advertisements resonate with your target audience and boost user engagement and conversion rates.

## Project Overview

TargetAd was created to tackle the challenge of delivering ads that truly matter to users. By utilizing demographic information such as age and gender, TargetAd crafts precise ad recommendations. Here's an overview of how the system operates:

1. **Webcam Data Collection**: TargetAd captures your facial features via your webcam, and a model accurately assesses your age and gender.

2. **Demographic Analysis**: TargetAd meticulously examines this demographic data and aligns it with predefined ad categories.

3. **Recommendations**: Leveraging the user's demographics, TargetAd suggests ads from relevant categories that are most likely to resonate with them.

4. **Ad Display**: These personalized advertisements are presented to the user through suitable channels, primarily using OpenCV Windows.

## Getting Started

To embark on your journey with TargetAd, follow these simple steps:

1. **Clone the Repository**: Begin by cloning this GitHub repository to your local machine.
  ```bash
   git clone https://github.com/Michael-RDev/TargetAd.git
  ```

2. **Create a Python Virtual Environment**: Establish a Python virtual environment to ensure a clean and isolated development environment.
 ```bash
  cd TargetAd
  ```
 Create a Python virtual environment 
 ```bash
 python -m venv .venv
  ```
  **Activate the Python virtual environment**
  
  Windows: 
  ```bash
  .venv/Scripts/activate
  ```
  Mac:
  ```bash
  source .venv/bin/activate
  ```
  

3. **Install Dependencies**: Navigate to the project directory and install all the necessary dependencies. This will ensure smooth execution of the program.
  ```bash
  pip install -r requirements.txt
  ```

**MAKE SURE TO CHANGE YOUR PATHS**

4. **Run the Program**: You're all set! Run the TargetAd program and experience the magic of personalized advertising recommendations based on age and gender.
  ```bash
    python main.py
  ```
