import unreal
import json
import os

# get contral pawn
player_controller = unreal.EditorLevelLibrary.get_level_player_controller(0)
pawn = player_controller.get_pawn()

loc = pawn.get_actor_location()
rot = pawn.get_actor_rotation()

pose = {
    "position": {
        "x": round(loc.x, 2),
        "y": round(loc.y, 2),
        "z": round(loc.z, 2)
    },
    "rotation": {
        "yaw": round(rot.yaw, 2),
        "pitch": round(rot.pitch, 2),
        "roll": round(rot.roll, 2)
    }
}

# output
output_path = os.path.expanduser("~/Desktop/pose_step0.json")
with open(output_path, "w") as f:
    json.dump(pose, f, indent=2)

print(f"[✓] Pose saved to: {output_path}")