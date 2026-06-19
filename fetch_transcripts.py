import os
import sys

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("Installing youtube-transcript-api...")
    os.system(f"{sys.executable} -m pip install youtube-transcript-api")
    from youtube_transcript_api import YouTubeTranscriptApi

VIDEOS = [
    ("ryan-law", "iVZrVeESnFQ", "How to automate blog writing with AI"),
    ("ryan-law", "b949h7ZJW8w", "Ryan Law on generative AI and content"),
    ("kevin-indig", "jxXPpXL2pFg", "Beyond the SERP Winning the Visibility Layer"),
    ("kevin-indig", "Aj6XR_1Ya2E", "Dominate Organic B2B Growth in the AI Era"),
    ("ross-simmonds", "7_bFP2iVVN0", "B2B Content Marketing and Distribution"),
    ("ross-simmonds", "8lQfWBFF45U", "B2B Content and Social Media Strategy"),
    ("kyle-byers", "fbv2-JtC5PM", "Googles Helpful Content Update Panel"),
    ("bernard-huang", "f84ovVChEh4", "AI driven SEO revolution discoverability"),
    ("koray-tugberk-gubur", "81pe-YM9iRI", "AI Powered Semantic SEO with Koray Gubur"),
    ("koray-tugberk-gubur", "8qr6vEUnFUM", "Koray Tugberk Gubur Invented Topical Authority"),
    ("aleyda-solis", "fbv2-JtC5PM", "Googles Helpful Content Update Aleyda Solis"),
]

OUTPUT_DIR = "research/youtube-transcripts"


def sanitize(text):
    return "".join(c if c.isalnum() or c in "-_ " else "" for c in text).strip().replace(" ", "-")


def fetch_and_save(expert, video_id, title):
    folder = os.path.join(OUTPUT_DIR, expert)
    os.makedirs(folder, exist_ok=True)
    filename = f"{sanitize(title)[:60]}.txt"
    filepath = os.path.join(folder, filename)

    if os.path.exists(filepath):
        print(f"  [SKIP] Already exists: {filepath}")
        return True

    try:
        ytt = YouTubeTranscriptApi()
        transcript_data = ytt.fetch(video_id)
        full_text = "\n".join(snippet.text for snippet in transcript_data)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"EXPERT: {expert}\n")
            f.write(f"VIDEO TITLE: {title}\n")
            f.write(f"VIDEO URL: https://www.youtube.com/watch?v={video_id}\n")
            f.write("-" * 60 + "\n\n")
            f.write(full_text)

        print(f"  [OK] Saved: {filepath}")
        return True

    except Exception as e:
        with open(filepath.replace(".txt", "_FAILED.txt"), "w") as f:
            f.write(f"Transcript unavailable for video: {video_id}\n")
            f.write(f"Reason: {str(e)}\n")
        print(f"  [FAIL] {expert} / {title[:40]} --- {e}")
        return False


def main():
    print("\n========================================")
    print("  AI SEO Transcript Fetcher")
    print("========================================\n")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    success = 0
    failed = 0
    current_expert = None

    for expert, video_id, title in VIDEOS:
        if expert != current_expert:
            print(f"\n-- {expert.upper()} --")
            current_expert = expert
        result = fetch_and_save(expert, video_id, title)
        if result:
            success += 1
        else:
            failed += 1

    print(f"\n========================================")
    print(f"  Done. {success} saved, {failed} failed.")
    print(f"========================================\n")


if __name__ == "__main__":
    main()