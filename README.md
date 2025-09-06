\# Telecommunications Data Processing and Storage System



A \*\*serverless data pipeline\*\* built on \*\*AWS\*\* that ingests raw telecom data (CSV), processes it using \*\*AWS Lambda\*\*, and stores the output as JSON for analysis.



\## 🚀 Features

\- Automated \*\*CSV → JSON conversion\*\* using Lambda and Python

\- Event-driven pipeline triggered by \*\*Amazon S3 uploads\*\*

\- Scalable, cost-efficient, and fully serverless

\- Secure execution using \*\*IAM roles\*\*



\## 🛠️ Tech Stack

\- \*\*Python 3.x\*\*

\- \*\*AWS Lambda\*\*

\- \*\*Amazon S3\*\*

\- \*\*Boto3 SDK\*\*



\## 📂 Project Structure

telecom-data-pipeline/

├── lambda\_functions/

│ └── csv\_to\_json.py # Lambda function for CSV → JSON conversion

├── sample\_data/

│ └── sample\_telecom.csv # Dummy data for testing

├── requirements.txt # Python dependencies

├── README.md # Project overview

├── .gitignore # Ignore unnecessary files

└── .env.example # Environment variable placeholders


\## ⚡ How It Works

1\. Upload CSV files to the S3 input bucket.  

2\. S3 triggers the Lambda function automatically.  

3\. Lambda converts the CSV data into JSON format.  

4\. JSON file is stored in the `processed/` folder in the same S3 bucket.  



\## 🔧 Setup Instructions (Local Demo)

1\. Clone the repo:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/praveen-0116/telecom-data-pipeline.git

&nbsp;  cd telecom-data-pipeline

2\. Create a virtual environment and install dependencies:
   python -m venv venv

&nbsp;  source venv/bin/activate   # Windows: venv\\Scripts\\Activate.ps1

&nbsp;  pip install -r requirements.txt

3\. Run the sample local script (optional):
   python lambda\_functions/csv\_to\_json.py

Notes



This repo uses dummy telecom data only



No real credentials or sensitive information are included



Environment variables should be defined in .env (see .env.example)



📧 Author



Patlolla Praveen

Email: patlollapraveen000@gmail.com



LinkedIn: https://www.linkedin.com/in/patlolla-praveen-509206214

