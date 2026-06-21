import os
import requests

SUPADATA_API_KEY = "sd_7750beb7d9e62d95d44d22fbda816f38"

VIDEOS = [
    ("ryan-law", "iVZrVeESnFQ", "How to automate blog writing with AI"),
    ("ryan-law", "b949h7ZJW8w", "Ryan Law on generative AI and content"),
    ("kevin-indig", "jxXPpXL2pFg", "Beyond the SERP Winning the Visibility Layer"),
    ("kevin-indig", "Aj6XR_1Ya2E", "Dominate Organic B2B Growth in the AI Era"),
    ("koray-tugberk-gubur", "81pe-YM9iRI", "AI Powered Semantic SEO with Koray Gubur"),
    ("koray-tugberk-gubur", "8qr6vEUnFUM", "Koray Tugberk Gubur Invented Topical Authority"),
    ("nathan-gotch", "7mtCa8sqjBo", "AI Changed SEO Forever Nathan Gotch 2025"),
    ("nathan-gotch", "4BSMNFNhY_E", "Nathan Gotch Playbook Breaking Through SEO with AI"),
    ("britney-muller", "l4fIHPtjIMY", "Breaking Down AI and Search Changes 2025"),
    ("britney-muller", "YZD2lmcbryo", "SEO is Changing Brand Mentions New Backlinks"),
    ("aleyda-solis", "fbv2-JtC5PM", "Googles Helpful Content Update Aleyda Solis"),
    ("brendan-hufford", "p3_P0dDspBI", "Brendan Hufford B2B SaaS SEO content"),
    ("wil-reynolds", "YVaRBvNXg6o", "SEO Industry Obsessed With Wrong AI Metric"),
    ("wil-reynolds", "0JzhxXHCTYY", "Future of Search AI Takes Over"),
    ("ross-hudgens", "8-PS7gR2G0I", "AI Visibility Data Journalism Future of SEO"),
    ("ross-hudgens", "1tr7nNrEYHk", "Evolving Content Marketing Playbook SEO Week"),
]

OUTPUT_DIR = "research/youtube-transcripts"


def sanitize(text):
    return "".join(c if c.isalnum() or c in "-_ " else "" for c in text).strip().replace(" ", "-")


def fetch_and_save(expert, video_id, title):
    folder = os.path.join(OUTPUT_DIR, expert)
    os.makedirs(folder, exist_ok=True)
    filename = sanitize(title)[:60] + ".txt"
    filepath = os.path.join(folder, filename)

    if os.path.exists(filepath):
        print("  [SKIP] Already exists: " + filepath)
        return True

    try:
        url = "https://api.supadata.ai/v1/youtube/transcript?videoId=" + video_id
        headers = {"x-api-key": SUPADATA_API_KEY}
        response = requests.get(url, headers=headers)
        data = response.json()

        if "content" not in data:
            raise Exception(str(data.get("error", "No content returned")))

        full_text = "\n".join(segment["text"] for segment in data["content"])

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("EXPERT: " + expert + "\n")
            f.write("VIDEO TITLE: " + title + "\n")
            f.write("VIDEO URL: https://www.youtube.com/watch?v=" + video_id + "\n")
            f.write("-" * 60 + "\n\n")
            f.write(full_text)

        print("  [OK] Saved: " + filepath)
        return True

    except Exception as e:
        with open(filepath.replace(".txt", "_FAILED.txt"), "w") as f:
            f.write("Transcript unavailable for video: " + video_id + "\n")
            f.write("Reason: " + str(e) + "\n")
        print("  [FAIL] " + expert + " / " + title[:40] + " --- " + str(e))
        return False


def main():
    print("\n========================================")
    print("  AI SEO Transcript Fetcher - Supadata")
    print("========================================\n")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    success = 0
    failed = 0
    current_expert = None

    for expert, video_id, title in VIDEOS:
        if expert != current_expert:
            print("\n-- " + expert.upper() + " --")
            current_expert = expert
        result = fetch_and_save(expert, video_id, title)
        if result:
            success += 1
        else:
            failed += 1

    print("\n========================================")
    print("  Done. " + str(success) + " saved, " + str(failed) + " failed.")
    print("========================================\n")


if __name__ == "__main__":
    main()