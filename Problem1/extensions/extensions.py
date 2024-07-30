def main():
    str = input("File name: ").strip().lower()
    if "gif" in str:
        print("image/gif")
    # elif "jpg" or "jpeg" in str:wrong way to code
    elif "jpg" in str or "jpeg" in str:
        print("image/jpeg")
    elif "png" in str:
        print("image/png")
    elif "pdf" in str:
        print("application/pdf")
    elif "txt" in str:
        print("text/plain")
    elif "zip" in str:
        print("application/zip")
    else:
        print("application/octet-stream")
main()
