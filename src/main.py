#
# Copyright (c) 2021 PAULA B. OLMEDO.
#
# This file is part of IMAGE_PROCESSOR
# (see https://github.com/paulaolmedo/sentinel-scripts).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.#
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
