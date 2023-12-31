import os
import saveOutputs

# in the cwd I have a file called reg.txt I want you to compare the output of the command "apt list --installed" to the contents of reg.txt
# if there is a difference, print the difference to the screen

def main():
    # open the file
    f = open("reg.txt", "r")
    # read the file
    reg = f.read()
    # close the file
    f.close()

    issues = []
    
    # run the command
    apt = os.popen("apt list --installed").read()
    
    # compare the two
    if reg != apt:
        # loop through the lines of the file
        for line in apt.splitlines():
            # if the line is not in the file
            if line not in reg and line != "Listing...":
                saveOutputs.warning("APT Package Discrepancy:")
                saveOutputs.warning("     " + line)
                issues.append(line)
    if issues == []:
        saveOutputs.success("No APT Package Discrepancies Found")