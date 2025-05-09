import unreal
import json
import os

# get all Actor
actors = unreal.EditorLevelLibrary.get_all_level_actors()
semantic_data = []

for actor in actors:
    name = actor.get_fname()
    tags = [str(tag) for tag in actor.tags]
    location = actor.get_actor_location()
    actor_class = actor.get_class().get_name()
    
    entry = {
        "name": str(name),
        "type": actor_class,
        "tags": tags,
        "location": {
            "x": location.x,
            "y": location.y,
            "z": location.z
        }
    }
    semantic_data.append(entry)

# save as json
output_path = os.path.expanduser("~/Desktop/semantic_map.json")  # location
with open(output_path, "w") as f:
    json.dump(semantic_data, f, indent=2)

print(f"Semantic map exported to: {output_path}")