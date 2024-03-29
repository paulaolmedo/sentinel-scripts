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
import re
import os
import zipfile
from os import path as check_path


class RenameRaster:
    def __init__(self, workdir):
        self.workdir = workdir

    def rename_raster_file(self):
        os.chdir(self.workdir)
        current_path = os.getcwd()

        ###################
        print("###################")
        print("starting renaming process of zipped folders")
        print("###################")
        ###################

        # regex para limpiar el nombre de los archivos comprimidos
        regex = r"(\d{8})"

        for current_file in os.listdir(current_path):
            if(check_path.isfile(current_file)):
                print("ABOUT TO RENAME: " + current_file)
                matches = re.finditer(regex, current_file)
                for match in matches:
                    temporal, file_extension = os.path.splitext(current_file)
                    new_filename = current_path + "/" + match.group() + file_extension
                    print("NEW FILENAME: " + new_filename)
                    os.rename(current_path + "/" + current_file, new_filename)

        # pausa para verificar que esté todo ok
        input("PRESS ANY KEY TO CONTINUE")

        ###################
        print("###################")
        print("starting unzipping process")
        print("###################")
        ###################

        # agrego un nuevo directorio para guardar los archivos descomprimidos
        if os.path.exists("unzipped") is False:
            os.mkdir("unzipped")

        # descomprimo los archivos necesarios
        for zipped_file in os.listdir(current_path):
            temporal, file_extension = os.path.splitext(zipped_file)
            if file_extension == ".zip":
                try:
                    with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
                        zip_ref.extractall("unzipped")
                        print("EXTRACTED: " + zipped_file)

                except zipfile.BadZipFile:
                    print("not a zipfile: " + zipped_file)

        # actualizo el directorio de trabajo a la carpeta de los archivos descomprimidos
        os.chdir("unzipped")
        updated_path = os.getcwd()

        if not os.listdir(updated_path):
            print("there were no raster folders to unzip :( exiting now")

        else:
            # pausa para verificar que esté todo ok
            input("PRESS ANY KEY TO CONTINUE")

            ###################
            print("###################")
            print("starting renaming process of unzipped folders")
            print("###################")
            ###################

            # regex para limpiar el nombre de los archivos descomprimidos (los SAFE)
            regex_safe = r"(MSIL1C_)(\d{8})"

            for unzipped_file in os.listdir(updated_path):
                matches = re.finditer(regex_safe, unzipped_file)
                for match in matches:
                    temporal, file_extension = os.path.splitext(unzipped_file)
                    new_filename = match.group() + file_extension
                    print("NEW FILENAME: " + new_filename)
                    os.rename(unzipped_file, new_filename)

            # pausa para verificar que esté todo ok
            input("PRESS ANY KEY TO CONTINUE")

            ###################
            print("###################")
            print("starting renaming process of folders under GRANULE PATH")
            print("###################")
            ###################

            # regex para limpiar el nombre de las carpetas correspondientes adentro de GRANULE
            regex = r"(\d{8})"

            for every_folder in os.listdir(updated_path):
                internal_path = updated_path + "/" + every_folder + "/GRANULE/"
                if check_path.isdir(internal_path):
                    for internal_folder in os.listdir(internal_path):
                        matches = re.finditer(regex, internal_folder)
                        for match in matches:
                            new_folder_name = internal_path + "MSIL1C_" + match.group()
                            print("NEW FOLDER NAME: " + new_folder_name)
                            os.rename(internal_path + internal_folder, new_folder_name)

            # pausa para verificar que esté todo ok
            input("PRESS ANY KEY TO CONTINUE")

            ###################
            print("###################")
            print("starting renaming process of spectral bands")
            print("###################")
            ###################

            # regex para actualizar el nombre de las bandas
            folder_path = os.getcwd()

            if check_path.isdir(folder_path):
                for current_folder in os.listdir(folder_path):
                    if(check_path.isdir(current_folder)):
                        internal_folder, file_extension = os.path.splitext(current_folder)
                        current_path_to_rename = folder_path + "/" + current_folder + "/GRANULE/" + internal_folder + "/IMG_DATA/"

                    regex = r"(B\d+\w)"

                    file_list = os.listdir(current_path_to_rename)
                    file_list.sort()

                    for i in range(len(file_list)):
                        current_file = file_list[i]
                        matches = re.finditer(regex, current_file)
                        for match in matches:
                            if(match.group() == "B01"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "blue_coast_443_60.jp2")
                            if(match.group() == "B02"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "blue_492_10.jp2")
                            if(match.group() == "B03"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "green_560_10.jp2")
                            if(match.group() == "B04"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "red_665_10.jp2")
                            if(match.group() == "B05"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir_705_20.jp2")
                            if(match.group() == "B06"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir2_740_20.jp2")
                            if(match.group() == "B07"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir3_783_20.jp2")
                            if(match.group() == "B08"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir4_832_10.jp2")
                            if(match.group() == "B8A"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir4a_865_20.jp2")
                            if(match.group() == "B09"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir_945_60.jp2")
                            if(match.group() == "B10"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir2_1373_60.jp2")
                            if(match.group() == "B11"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir3_1614_20.jp2")
                            if(match.group() == "B12"):
                                os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir4_2202_20.jp2")

            print("ALLES GUT")
