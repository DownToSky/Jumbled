from pypresence import Presence
import time

client_id = '580120822736355338'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Playing with the BOIS", details="Derping off the face of the earth",large_image="drp",small_image="hrt",party_size=[69,420]))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
