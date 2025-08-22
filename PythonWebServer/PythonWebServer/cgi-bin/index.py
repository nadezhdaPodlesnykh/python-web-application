#!/usr/bin/env python3



def printChatMessages(data):
    #data enters only onсe
    current_date = None 

    for i in range(0, len(data), 2):
        date_time_str = data[i]
        message = data[i + 1]

        date_part, time_part = date_time_str.split(' - ')

        
        if current_date != date_part:
            current_date = date_part
            # when day is changed, date appears again
            print(f"<div class='chat-date'>{current_date}</div>") 

        # display message with time
        print(f"<div class='chat-message'>")
        print(f"<div class='chat-time'>{time_part}</div>")
        print(f"<div class='chat-text'>{message}</div>")
        print(f"</div>")

print("Content-Type: text/html") 
print()

print("<html><body>")


print("""
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4;
    }

    .chat-container {
        width: 500px;
        margin: auto;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
        overflow-y: auto;
        max-height: 400px;
    }

    .chat-date {
        text-align: center;
        font-size: 14px;
        color: #999;
        margin: 20px 0 10px;
        font-weight: bold;
    }

    .chat-message {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 8px;
        background-color: #e7e7e7;
    }

    .chat-time {
        font-size: 12px;
        color: #555;
        margin-bottom: 5px;
        text-align: right;
    }

    .chat-text {
        font-size: 14px;
        color: #333;
    }

    .chat-message:nth-child(even) {
        background-color: #d4f7db;
    }

    .chat-message:nth-child(odd) {
        background-color: #f1f1f1;
    }

    form {
        margin-top: 20px;
    }

    input[type="text"] {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 14px;
    }

    input[type="submit"] {
        padding: 10px 20px;
        border: none;
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        margin-top: 10px;
    }

    input[type="submit"]:hover {
        background-color: #45a049;
    }
</style>
""")


dataFilePath = 'myData/myData.txt'
myData = []
with open(dataFilePath, 'r') as file:
    myData = [line.strip() for line in file]

print("<div class='chat-container'>")
printChatMessages(myData)
print("</div>")


print("""
<form action="add_record.py">
  <label for="mytext">Write a message:</label><br>
  <input type="text" id="mytext" name="mytext" placeholder="Enter your message" required><br>
  <input type="submit" value="Send">
</form>
""")

print("</body></html>")
