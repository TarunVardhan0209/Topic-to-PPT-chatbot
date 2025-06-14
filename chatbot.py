from api_client import get_ppt_json
from ppt_generator import create_ppt

def main():
    topic = input("📌 Enter the topic for the presentation:\n")
    print("⏳ Generating slides, please wait...")

    try:
        slides_json = get_ppt_json(topic)
        print("✅ Slides generated!")

        output_path = create_ppt(slides_json, topic)
        print(f"📄 PowerPoint saved at: {output_path}")

    except Exception as e:
        print(f"❌ Failed to create PPT: {e}")

if __name__ == "__main__":
    main()
