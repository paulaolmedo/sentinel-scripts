import re
import os
import zipfile
from os import path as check_path

os.chdir(".") #indico que el directorio de trabajo es en el que estoy parada
current_path = os.getcwd()

#regex para limpiar el nombre de los archivos comprimidos
regex = r"(\d{8})"

for current_file in os.listdir(current_path):
    if(check_path.isfile(current_file)):
        print("ABOUT TO RENAME: " + current_file)
        matches = re.finditer(regex, current_file)
        for match in matches:
            temporal, file_extension = os.path.splitext(current_file)
            new_filename = current_path +"/"+ match.group() + file_extension
        
            os.rename(current_path +"/"+ current_file, new_filename)

#agrego un nuevo directorio para guardar los archivos descomprimidos
os.mkdir("unzipped") 

#descomprimo los archivos necesarios
for zipped_file in os.listdir(current_path):
    temporal, file_extension = os.path.splitext(zipped_file)
    if file_extension == ".zip":
        with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("unzipped")


#actualizo el directorio de trabajo a la carpeta de los archivos descomprimidos
os.chdir("unzipped")
updated_path  = os.getcwd()

#regex para limpiar el nombre de los archivos descomprimidos (los SAFE)
regex_safe = r"(MSIL1C_)(\d{8})"

for unzipped_file in os.listdir(updated_path):
    matches = re.finditer(regex_safe, unzipped_file)
    for match in matches:
        temporal, file_extension = os.path.splitext(unzipped_file)
        new_filename = match.group() + file_extension
        os.rename(unzipped_file, new_filename)

#regex para limpiar el nombre de las carpetas correspondientes adentro de GRANULE
regex = r"(\d{8})"

for every_folder in os.listdir(updated_path):
    internal_path = updated_path + "/" + every_folder + "/GRANULE/"
    #print(internal_path)
    if check_path.isdir(internal_path):
        for internal_folder in os.listdir(internal_path):
            #print(internal_folder)
            matches = re.finditer(regex, internal_folder)
            for match in matches:
                new_folder_name = internal_path + "MSIL1C_" + match.group()
                #print(new_folder_name)
                os.rename(internal_path + internal_folder, new_folder_name)


#regex para actualizar el nombre de las bandas
band_name_remap_dict = {
    "B01": "blue_coast_443_60.jp2",
    "B02": "blue_492_10.jp2",
    "B03": "green_560_10.jp2",
    "B04": "red_665_10.jp2",
    "B05": "nir_705_20.jp2",
    "B06": "nir2_740_20.jp2",
    "B07": "nir3_783_20.jp2",
    "B08": "nir4_832_10.jp2",
    "B8A": "nir4a_865_20.jp2",
    "B09": "swir_945_60.jp2",
    "B10": "swir2_1373_60.jp2",
    "B11": "swir3_1614_20.jp2", 
    "B12": "swir4_2202_20.jp2"
}

folder_path = os.getcwd()


if check_path.isdir(folder_path):
    for current_folder in os.listdir(folder_path):
        if(check_path.isdir(current_folder)):
            internal_folder, file_extension = os.path.splitext(current_folder)
            current_path_to_rename = folder_path + "/"+  current_folder + "/GRANULE/" + internal_folder + "/IMG_DATA/"
            #print(current_path_to_rename)

        regex = r"(B\d+\w)"

        file_list = os.listdir(current_path_to_rename)
        file_list.sort()

        for current_file in file_list:
            #current_file = file_list[i]
            matches = re.finditer(regex, current_file)
            #print(current_file)
            for match in matches:
                for key in band_name_remap_dict:
                    if(match.group()==key):
                        os.rename(current_path_to_rename + current_file, current_path_to_rename + band_name_remap_dict[key])
    
