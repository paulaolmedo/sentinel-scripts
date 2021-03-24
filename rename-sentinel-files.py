import re
import os
import zipfile
from os import path as check_path

os.chdir(".") #indico que el directorio de trabajo es en el que estoy parada
current_path = os.getcwd()

###################
print("###################")
print("starting renaming process of zipped folders")
print("###################")
###################

#regex para limpiar el nombre de los archivos comprimidos
regex = r"(\d{8})"

for current_file in os.listdir(current_path):
    if(check_path.isfile(current_file)):
        print("ABOUT TO RENAME: " + current_file)
        matches = re.finditer(regex, current_file)
        for match in matches:
            temporal, file_extension = os.path.splitext(current_file)
            new_filename = current_path +"/"+ match.group() + file_extension
            print("NEW FILENAME: " + new_filename)
            os.rename(current_path +"/"+ current_file, new_filename)

#pausa para verificar que esté todo ok
input("PRESS ANY KEY TO CONTINUE")

###################
print("###################")
print("starting unzipping process")
print("###################")
###################

#agrego un nuevo directorio para guardar los archivos descomprimidos
os.mkdir("unzipped")

#descomprimo los archivos necesarios
for zipped_file in os.listdir(current_path):
    temporal, file_extension = os.path.splitext(zipped_file)
    if file_extension == ".zip":
        with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("unzipped")
            print("EXTRACTED: " + zipped_file)

#pausa para verificar que esté todo ok
input("PRESS ANY KEY TO CONTINUE")

###################
print("###################")
print("starting renaming process of unzipped folders")
print("###################")
###################

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
        print("NEW FILENAME: " + new_filename)
        os.rename(unzipped_file, new_filename)

#pausa para verificar que esté todo ok
input("PRESS ANY KEY TO CONTINUE")

###################
print("###################")
print("starting renaming process of folders under GRANULE PATH")
print("###################")
###################

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
                print("NEW FOLDER NAME: " + new_folder_name)
                os.rename(internal_path + internal_folder, new_folder_name)


#pausa para verificar que esté todo ok
input("PRESS ANY KEY TO CONTINUE")

###################
print("###################")
print("starting renaming process of spectral bands")
print("###################")
###################

#regex para actualizar el nombre de las bandas
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

        for i in range(len(file_list)):
            current_file = file_list[i]
            matches = re.finditer(regex, current_file)
            #print(current_file)
            for match in matches:
                #print(match.group())
                if(match.group()=="B01"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "blue_coast_443_60.jp2")
                if(match.group()=="B02"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "blue_492_10.jp2")
                if(match.group()=="B03"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "green_560_10.jp2")
                if(match.group()=="B04"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "red_665_10.jp2")
                if(match.group()=="B05"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir_705_20.jp2")
                if(match.group()=="B06"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir2_740_20.jp2")
                if(match.group()=="B07"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir3_783_20.jp2")
                if(match.group()=="B08"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir4_832_10.jp2")
                if(match.group()=="B8A"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "nir4a_865_20.jp2")
                if(match.group()=="B09"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir_945_60.jp2")
                if(match.group()=="B10"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir2_1373_60.jp2")
                if(match.group()=="B11"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir3_1614_20.jp2")
                if(match.group()=="B12"):
                    os.rename(current_path_to_rename + current_file, current_path_to_rename + "swir4_2202_20.jp2")
            
print("ALLES GUT")
