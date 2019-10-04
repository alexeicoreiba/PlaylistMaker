''' writes all supported file names 
    in file_path to output.m3u
    (string, string) -> None
'''


def PlaylistMaker(file_path, output):
    extensions = [".mp3", ".flac", ".aac", ".m4a"]
    with open(output + ".m3u", "w", encoding="utf-8") as outputFile:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if any(x in file for x in extensions):
                    outputFile.write(file + "\n")
    print("Playlist saved successfully in " + output + ".m3u")


if __name__ == "__main__":
    import os
    import sys
    import getopt

    def usage():
        print('Usage:    ' + os.path.basename(__file__) + ' directory')
        sys.exit(2)
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "hedk:o:", ["help"])
    except getopt.GetoptError as err:
        print(err)
        usage()
    # extract parameters
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
    if len(args) == 1:
        file = args[0]
        outputFile = os.path.basename(os.path.normpath(file))
    else:
        usage()
    PlaylistMaker(file, outputFile)
