from awpy import Demo
import sys

demo = Demo(sys.argv[1], verbose=True)
demo.parse(player_props=["name", "side", "user_id", "entity_id"])



# Get unique (user_id, name) pairs as a list of tuples
unique_pairs = demo.ticks.select(["user_id", "name", "side"]).unique(subset=["user_id", "name"], keep="first").rows()

# Emit arrays where side == 'ct' and side == 't'
ct_players = [row for row in unique_pairs if row[2] == 'ct']
t_players = [row for row in unique_pairs if row[2] == 't']


print("\nCT players:")
print(ct_players)

print("\nT players:")
print(t_players)

# Function to create a binary bitmap from a player array (using user_id)
def create_player_bitmap(player_array):
	bitmap = 0
	for row in player_array:
		user_id = row[0]
		if isinstance(user_id, int) and user_id >= 0:
			bitmap |= (1 << user_id)
	return bitmap

# Create and print bitmaps
ct_bitmap = create_player_bitmap(ct_players)
t_bitmap = create_player_bitmap(t_players)


print("\nCT bitmap:", bin(ct_bitmap))
print("tv_listen_voice_indices_h", ct_bitmap)
print("tv_listen_voice_indices", ct_bitmap)

print("\nT bitmap:", bin(t_bitmap))
print("tv_listen_voice_indices_h", t_bitmap)
print("tv_listen_voice_indices", t_bitmap)

