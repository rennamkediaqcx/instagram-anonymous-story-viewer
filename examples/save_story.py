from src.tools.story_saver import StorySaver

def main():
    saver = StorySaver()
    print("StorySaver is ready. Call saver.save(url=..., output_dir='downloads') with a direct URL you are permitted to download.")

if __name__ == "__main__":
    main()
