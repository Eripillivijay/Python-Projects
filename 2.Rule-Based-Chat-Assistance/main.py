import datetime
import time

# Greeting User
name = input("Welcome, enter your name: ")
presentHour = datetime.datetime.now().hour
time.sleep(1)
if 5 <= presentHour <= 11:
    print("Good Morning🙏: ", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon🙏: ", name)
elif 17 <= presentHour <= 20:
    print("Good Evening🙏: ", name)
else:
    print("Good Night🙏: ", name)

print("Welcome to the ChatBot")
print("You can ask me the basic questions. Type 'bye' to exit from the AI Bot")

 
#Chatbot Memory Creation
responses = {
    "hello" : f"Welcome {name}. How Can I help you?",
    "how are you": f"I am  fine {name}. Thank you for asking",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": f"Great to hear that from you {name}",
    "python": "Python is a versatile, high-level programming language known for its simple, English-like syntax and readability. It is widely used for building websites, automating repetitive tasks, analyzing data, and developing artificial intelligence. Because it is beginner-friendly, it is popular with both software engineers and non-programmers.",
    "bye": f"Thank you for your time {name}"
}

# Method to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell that yet. I am in a learning phase"

# Take User Input
while True:
    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    time.sleep(1)
    print("Bot Response: ",reply)

    if "bye" in userInput.lower():
        break