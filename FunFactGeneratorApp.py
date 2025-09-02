import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

# Function to fetch and display a fun fact when the button is clicked
def get_fun_fact(_):
    # Clear previous output from the screen
    clear()

    # Display heading with an image (Fun Fact Generator title)
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="10%"> Fun Fact Generator App</h2>'
        '</p>'
    )

    # API URL to fetch a random fun fact
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Send GET request to API
    response = requests.get(url)

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract the fact text
    fact = data['text']

    # Display the fun fact with custom styling (blue color, large font size)
    style(put_text(fact), 'color:orange; font-size: 40px')

    # Add a button that calls `get_fun_fact` again when clicked (for another fact)
    put_buttons(
        [dict(label='Click for Fun', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

# Entry point of the script
if __name__ == '__main__':
    # Display initial heading with image
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="10%"> Fun Fact Generator App</h2>'
        '</p>'
    )
    
    # Display initial button to start generating fun facts
    put_buttons(
        [dict(label='Click for Fun', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

    # Keep the session alive so the UI remains responsive
    hold()
