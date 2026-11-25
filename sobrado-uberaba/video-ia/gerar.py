#!/usr/bin/env python3
"""Gera os 8 clipes do tour (imagem para vídeo) pela API da MuAPI.

A chave não fica neste arquivo: o proxy do ambiente injeta o header
x-api-key em toda chamada a api.muapi.ai. Rodar a partir desta pasta:
    python3 gerar.py [modelo]
"""
import json, os, sys, time, urllib.request, uuid

BASE = "https://api.muapi.ai/api/v1"
MODEL = sys.argv[1] if len(sys.argv) > 1 else "kling-v3.0-standard-image-to-video"
HDR = {"x-api-key": "proxy-injected"}
NEG = " Keep architecture, walls and furniture straight and unchanged. No people, no text."

SHOTS = [
    ("01-fachada", "Slow smooth camera push-in toward the front door along the paved condominium street, steady gimbal, soft daylight, gentle breeze moving the palm leaves."),
    ("02-sala-jantar", "Slow lateral gimbal glide from left to right revealing the living and dining room, steady and calm, natural window light."),
    ("03-cozinha", "Slow smooth dolly forward along the kitchen island, subtle parallax, warm natural light."),
    ("04-escada", "Slow gentle upward tilt following the staircase, steady camera, soft daylight."),
    ("05-quarto", "Slow smooth push-in into the bedroom toward the window, calm steady movement, soft morning light."),
    ("06-home-office", "Slow pull-back revealing the home office and built-in shelf, steady camera, soft daylight."),
    ("07-banheiro", "Very slow short push-in toward the glass shower, steady, bright clean light."),
    ("08-sala-pet", "Very slow gentle push-in toward the small white dog on the sofa, the dog blinks and slightly tilts its head, cozy warm light."),
]


def req(method, url, data=None, headers=None):
    r = urllib.request.Request(url, data=data, method=method, headers={**HDR, **(headers or {})})
    with urllib.request.urlopen(r, timeout=120) as resp:
        return json.loads(resp.read())


def upload(path):
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{os.path.basename(path)}\"\r\n"
            "Content-Type: image/jpeg\r\n\r\n").encode() + open(path, "rb").read() + f"\r\n--{b}--\r\n".encode()
    d = req("POST", f"{BASE}/upload_file", body, {"Content-Type": f"multipart/form-data; boundary={b}"})
    return d.get("url") or d.get("file_url") or d["data"]["url"]


def main():
    os.makedirs("clipes", exist_ok=True)
    jobs = {}
    for name, prompt in SHOTS:
        if os.path.exists(f"clipes/{name}.mp4"):
            continue
        img = upload(f"{name}.jpg")
        payload = {"prompt": prompt + NEG, "image_url": img, "duration": 5, "aspect_ratio": "9:16"}
        d = req("POST", f"{BASE}/{MODEL}", json.dumps(payload).encode(), {"Content-Type": "application/json"})
        jobs[name] = d.get("request_id") or d.get("id")
        print("enviado", name, jobs[name], flush=True)
    while jobs:
        time.sleep(10)
        for name, rid in list(jobs.items()):
            d = req("GET", f"{BASE}/predictions/{rid}/result")
            st = d.get("status")
            if st == "completed":
                url = (d.get("outputs") or [None])[0]
                urllib.request.urlretrieve(url, f"clipes/{name}.mp4")
                print("pronto", name, flush=True)
                del jobs[name]
            elif st == "failed":
                print("FALHOU", name, d.get("error"), flush=True)
                del jobs[name]


if __name__ == "__main__":
    main()
