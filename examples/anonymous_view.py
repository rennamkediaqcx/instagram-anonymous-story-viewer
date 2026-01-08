from src.core.anonymous_viewer import AnonymousStoryViewer

def main():
    viewer = AnonymousStoryViewer()
    url = viewer.view_profile_anonymously("instagram")
    print("Opened:", url)

if __name__ == "__main__":
    main()
