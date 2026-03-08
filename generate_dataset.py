import csv
import random

data = [
("Adds two integers and returns sum","int a int b","int","MathUtils","add sum arithmetic",2,"addNumbers"),
("Subtracts second number from first","int a int b","int","MathUtils","subtract minus arithmetic",2,"subtractNumbers"),
("Multiplies two integers","int a int b","int","MathUtils","multiply product arithmetic",2,"multiplyNumbers"),
("Divides two integers","int a int b","float","MathUtils","divide arithmetic",2,"divideNumbers"),
("Calculates average of numbers","int a int b","float","StatsUtils","average mean stats",2,"calculateAverage"),
("Finds maximum of two numbers","int a int b","int","MathUtils","max compare",2,"findMax"),
("Finds minimum of two numbers","int a int b","int","MathUtils","min compare",2,"findMin"),
("Converts Celsius to Fahrenheit","float c","float","TempUtils","convert temperature",1,"convertCelsiusToFahrenheit"),
("Converts Fahrenheit to Celsius","float f","float","TempUtils","convert temperature",1,"convertFahrenheitToCelsius"),
("Reads file content","String path","String","FileUtils","read file",1,"readFile"),
("Writes content to file","String path String data","boolean","FileUtils","write save file",2,"writeFile"),
("Deletes file","String path","boolean","FileUtils","delete remove file",1,"deleteFile"),
("Parses JSON string","String json","JSONObject","JsonUtils","json parse",1,"parseJson"),
("Sends HTTP GET request","String url","HttpResponse","NetworkService","http api request",1,"sendGetRequest"),
("Sends HTTP POST request","String url String body","HttpResponse","NetworkService","http api post",2,"sendPostRequest"),
("Encrypts password","String password","String","SecurityUtils","encrypt password",1,"encryptPassword"),
("Decrypts password","String encrypted","String","SecurityUtils","decrypt password",1,"decryptPassword"),
("Generates random number","int min int max","int","RandomUtils","random generate number",2,"generateRandomNumber"),
("Sorts integer array","int[] arr","int[]","ArrayUtils","sort array",1,"sortArray"),
("Searches element in array","int[] arr int key","int","ArrayUtils","search find array",2,"searchElement")
]

with open("functions_dataset.csv","w",newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["description","parameters","return_type","library","keywords","param_count","function_name"])

    for i in range(2000):
        row = random.choice(data)
        writer.writerow(row)

print("Dataset generated: 2000 rows")