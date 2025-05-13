import unreal
import json
import os

# get agent name
agent_class_name = "ThirdPersonCharacter"

# search all actor
actors = unreal.EditorLevelLibrary.get_all_level_actors()

# find agent in actor list
pawn = next((a for a in actors if agent_class_name in a.get_class().get_name()), None)

if pawn:
    loc = pawn.get_actor_location()
    rot = pawn.get_actor_rotation()

    pose = {
        "position": {"x": round(loc.x, 2), "y": round(loc.y, 2), "z": round(loc.z, 2)},
        "rotation": {"yaw": round(rot.yaw, 2), "pitch": round(rot.pitch, 2), "roll": round(rot.roll, 2)}
    }

    # output json
    output_path = "C:/SimLLM-Nav/output_pos_file/pose_step0.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(pose, f, indent=2)

    print(f"[✓] Pose exported to: {output_path}")
else:
    print("[✗] No matching actor found in scene.")