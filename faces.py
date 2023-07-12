
def convert(faces):
    face = faces.replace(":)", "🙂").replace(":(", "🙁")
    return(face)

def main():
    face = input("")
    print(convert(face))

main()