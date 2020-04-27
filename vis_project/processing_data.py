import boto3
import botocore
import csv
import json

def lambda_handler():

    #download csv from s3 bucket
    BUCKET_NAME = 'slsbucket393' #  my bucket name
    KEY = 'horario.csv' # object key

    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'horario.csv')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    #csv - json converter
    csvFilePath = 'horario.csv'
    jsonFilePath = 'horario2.json'

    #read csv file and add to data
    data = {}
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            id = rows['id']
            data[id] =rows

    #create json file and write data on it
    with open(jsonFilePath, 'w') as jsonFile:
        #make it more readable and pretty
        jsonFile.write(json.dumps(data, indent=4))


lambda_handler()
