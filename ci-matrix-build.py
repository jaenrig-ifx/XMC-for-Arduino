

# check command lines arguments 
# The third value is the os name
import sys

# if len(sys.argv) != 2:
#     print("Usage: python ci-matrix-build.py <os> --check")
#     sys.exit(1)

# os = sys.argv[1]

# if (len(sys.argv) == 3 and sys.argv[2] == "--check"):

#     # check if the os is valid
#     if os == "ubuntu-latest" or os == "windows-latest":
#         print('true')
#     else:
#         print('false')
#         sys.exit(0)

# else:
#     if os == "ubuntu-latest":
#         matrix = '{ "fqbn": [ "Infineon:xmc:XMC1100_Boot_Kit", "Infineon:xmc:XMC1100_XMC2GO", "Infineon:xmc:XMC1300_Boot_Kit", "Infineon:xmc:XMC4200_Platform2GO", "Infineon:xmc:XMC4400_Platform2GO", "Infineon:xmc:XMC4700_Relax_Kit", "Infineon:xmc:XMC1400_XMC2GO", "Infineon:xmc:XMC1400_Arduino_Kit" ], "example": ["libraries/LED/examples/SimpleLED/SimpleLED.ino"] }' 
#     elif os == "windows-latest":
#         matrix = '{ "fqbn": [ "Infineon:xmc:XMC1100_Boot_Kit", "Infineon:xmc:XMC1100_XMC2GO", "Infineon:xmc:XMC1300_Boot_Kit", "Infineon:xmc:XMC4200_Platform2GO", "Infineon:xmc:XMC4400_Platform2GO", "Infineon:xmc:XMC4700_Relax_Kit", "Infineon:xmc:XMC1400_XMC2GO", "Infineon:xmc:XMC1400_Arduino_Kit" ], "example": ["libraries/LED/examples/SimpleLED/SimpleLED.ino"] }' 
#     elif os == "macos-latest":
#         matrix = '{ "fqbn": [ ] }'
#     else:
#         print("Unknown OS: " + os)
#         sys.exit(1)

matrix = '{ "fqbn": [ "Infineon:xmc:XMC1100_Boot_Kit", "Infineon:xmc:XMC1100_XMC2GO", "Infineon:xmc:XMC1300_Boot_Kit", "Infineon:xmc:XMC4200_Platform2GO", "Infineon:xmc:XMC4400_Platform2GO", "Infineon:xmc:XMC4700_Relax_Kit", "Infineon:xmc:XMC1400_XMC2GO", "Infineon:xmc:XMC1400_Arduino_Kit" ], "example": ["libraries/LED/examples/SimpleLED/SimpleLED.ino"] }' 
print(matrix)