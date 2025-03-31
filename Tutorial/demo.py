import requests 
from bs4 import BeautifulSoup

def decode_secret_message(url):

    #Fetch an HTTP request using URL and retrieve HTML content if successful  
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the document.")
        return

    #Parse HTML Content for relevant data using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    coor = {}
    
    
    #Strip Text from HTML element and assign coordinates to each character extracted into coor dictionary
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            if (x, y) not in coor:
                coor[(x, y)] = char
    
    return coor

def display_grid(data):
    # Check if the dictionary is empty
    if not data:
        print("No data to assemble.")
        return
    
    # Determine the grid size by finding maximum x and y coordinates
    max_x = max(x for x, _ in data.keys())  
    max_y = max(y for _, y in data.keys())  
    
    # Initialize the grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Place characters in the grid at their coordinates
    for (x, y), char in data.items():
        grid[y][x] = char

    # Reverse the order of the grid array 
    reversed_grid = grid[::-1]
    
    # Print each row of the reversed grid
    for row in reversed_grid:
        print(''.join(row))


url  = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
grid_data = decode_secret_message(url)

if grid_data:
    display_grid(grid_data)