from sys import argv
script, txtfile = argv

# Open the file using a with statement to ensure it's properly closed when done
with open(txtfile, 'r') as file:
    # Read the file contents
    lines = file.readlines()

# Initialize empty lists to store artist and track information
artists = []
tracks = []

# Process each line in the file
for line in lines:
    # Split the line by tab ('\t') to extract artist and track
    data = line.strip().split('\t')
    
    # Check if there are at least two elements in data
    if len(data) >= 2:
        artist = data[3]
        track = data[0]
        
        # Append artist and track to their respective lists
        artists.append(artist)
        tracks.append(track)

# Open the file again in write mode to overwrite its contents
with open(txtfile, 'w') as file:
    # Write the extracted artist and track information back to the file
    for artist, track in zip(artists, tracks):
        file.write(f"{artist} - {track}\n")

print(f"Data has been written to {txtfile}")