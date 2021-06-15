# Phys002-Project
This is related to our Nile University PHYS002 project.

## Team members
1. Abdelrahman A.
2. Marwan M.
3. Mostafa A.
4. Nadine A.
5. Omar E.

## This is a GUI tool for defining certain values in an arduino file. It is supposed to make the user define:-

1.The distance between the sensor and the container
2.The container's depth.
3.And the maximum water level (where the arduino prints an "Off" status if this value is reached)

## The files:-

1. ANgui.py: This is the main gui file
2. the text files with the .txtcon extension are there for testing the application's write functionality (Deprecated: file can directly affect main file now)
3. The other files are for testing purposes.
4. codetest.ino and codetest.c are for testing purposes as well.
5. ".gitignore" this is to ignore some dummy/testing/etc files.
6. The mainfiles contain mainfiles that were used for development.
7. The FinalExe directory contains releases and spec files used. You can use these with pyinstaller to rebuild the binaries. Icons and images are included.

## Important note:

In order for the gui to run, you need to have python3 installed with pip.

You also need to install ttkthemes using pip.

You can do so by issuing the following command in the terminal:-

          pip install ttkthemes
or

          pip3 install ttkthemes
          
You can freeze it with any freezing tool. For example: pyinstaller.

## Important note 2:

For linux binary users, you have to set the appropariate permissions for the binary.

          chmod +x binaryname

should work.

# Regards,

Team Aleph Node.
