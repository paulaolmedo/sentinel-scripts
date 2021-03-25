import sys
from rename_sentinel_files import RenameRaster

if sys.argv[1] == "--path":
    current_path = sys.argv[2]
    print("Current path is: \n" + current_path)

    user_response = input("is this right? press y/n \n")
    if user_response == "y":
        print(":)")
        rename_raster = RenameRaster(current_path)
        rename_raster.rename_raster_file()
    else:
        print(":(")
else:
    print("Invalid option: " + sys.argv[1] + ", please try again")
