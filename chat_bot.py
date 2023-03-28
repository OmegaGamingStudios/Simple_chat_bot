from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def search(searchs):
    search_query = searchs

    # Configure the webdriver to run headlessly
    options = Options()
    options.add_argument("--headless")

    # Start the webdriver and open Google
    print("searching...")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/")

    # Find the search box and input the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)

    # Submit the query
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load and click on the first link
    print("Getting the results...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g")))
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    first_result = search_results[0].find_element(By.TAG_NAME, "a")
    first_result.click()

    # Wait for the website to load and extract all the text within <p> tags
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    first_paragraphs = ""
    for p in paragraphs:
        if p:
            if len(first_paragraphs.split("\n")) >= 3:  # break if we have 3 paragraphs
                break
            first_paragraphs += p.text + "\n"

    # Print the first three paragraphs
    print(first_paragraphs)

    # Close the webdriver
    driver.quit()


# Define the User's responses
greeting = ('hi', 'hello', 'hi there')
thankyou = ('nice', 'good job', 'well done')
welcome = ('thank you', 'thanks')
bye = ('bye', 'goodbye', 'see you later')
whatsup = ('how are you', "what's up", 'you fine')
responsess = [greeting, thankyou, welcome, bye, whatsup]

# Define the bot's responses
responses = {
    responsess[0]: ["Hello!", "Hi there!", "Hey!"],
    responsess[4]: ["I'm good, thanks for asking.", "I'm doing well, how about you?", "Not much, how about you?",
                    "Just hanging out, you?"],
    responsess[2]: ["welcome", "Happy to help ", "Glad to hear"],
    responsess[1]: ["welcome", "Happy to help ", "Glad to hear"],
    responsess[3]: ["Goodbye!", "See you later!", "Bye for now!"],
    "default": ["I'm sorry, I didn't understand what you said.", "Could you please rephrase that?"]
}


# Define the chat function
def chat():
    print("Hi, I'm a chatbot. What can I help you with today?")
    while True:
        tuple_index = None
        user_input = input("You: ")
        for index, tup in enumerate(responsess):
            if user_input in tup:
                tuple_index = index
                user = responsess[tuple_index]
                bot_response = random.choice(responses[user])
                break

        else:
            bot_response1 = input("Should I search in google:")
            if bot_response1 == 'yes':
                search(user_input)
                continue
            else:
                bot_response = random.choice(responses["default"])

        print("Bot: " + bot_response)


# Call the chat function
chat()
