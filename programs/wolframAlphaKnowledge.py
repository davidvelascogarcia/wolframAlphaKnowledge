'''
 * ************************************************************
 *      Program: Wolfram Alpha Knowledge
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 *
 * | INPUT PORT                           | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /wolframAlphaKnowledge/data:i        | Input data text to resolve                              |
 *
 * | OUTPUT PORT                          | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /wolframAlphaKnowledge/data:o        | Output text result                                      |
 *
'''

# Libraries
import configparser
import datetime
import os
import platform
import time
import wolframalpha
import yarp


print("**************************************************************************")
print("**************************************************************************")
print("                   Program: Wolfram Alpha Knowledge                       ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading Wolfram Alpha Knowledge engine ...")
print("")

print("")
print("Initializing wolframAlphaKnowledge engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("Authentication:")
print("**************************************************************************")
print("")

# Variable loopControlFileExists
loopControlFileExists = 0

while int(loopControlFileExists) == 0:
    try:
        # Get autentication data
        print("")
        print("Getting authentication data ...")
        authenticationObject = configparser.ConfigParser()
        authenticationObject.read('../config/authentication.ini')
        authenticationObject.sections()

        userID = authenticationObject['Authentication']['user-id']
        accessToken = authenticationObject['Authentication']['access-token']
        loopControlFileExists = 1

    except:
        print("")
        print("[ERROR] Sorry, athentication.ini not founded, waiting 4 seconds to the next check ...")
        print("")
        time.sleep(4)

print("")
print("[INFO] Data obtained correctly.")
print("")
print("Selected user: " + str(userID))
print("")


print("")
print("**************************************************************************")
print("Wolfram Alpha client:")
print("**************************************************************************")
print("")
print("Configuring Wolfram Alpha authentication client ...")
print("")

# Build wolframAlphaKnowledge client
wolframAlphaClient = wolframalpha.Client(str(accessToken))

print("")
print("[INFO] Client configuration done at " + str(datetime.datetime.now()) + ".")
print("")

print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /wolframAlphaKnowledge/data:i ...")
print("")

# Open wolframAlphaKnowledge input data port
wolframAlphaKnowledge_inputPort = yarp.Port()
wolframAlphaKnowledge_inputPortName = '/wolframAlphaKnowledge/data:i'
wolframAlphaKnowledge_inputPort.open(wolframAlphaKnowledge_inputPortName)

# Create wolframAlphaKnowledge input data bottle
wolframAlphaKnowledgeInputBottle = yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /wolframAlphaKnowledge/data:o ...")
print("")

# Open wolframAlphaKnowledge output data port
wolframAlphaKnowledge_outputPort = yarp.Port()
wolframAlphaKnowledge_outputPortName = '/wolframAlphaKnowledge/data:o'
wolframAlphaKnowledge_outputPort.open(wolframAlphaKnowledge_outputPortName)

# Create wolframAlphaKnowledge output data bottle
wolframAlphaKnowledgeOutputBottle = yarp.Bottle()

print("")
print("[INFO] YARP network configured correctly.")
print("")

# Variable to control loopControlRequest
loopControlRequest = 0

while int(loopControlRequest) == 0:

    # Waiting to wolframAlphaKnowledge input data
    print("")
    print("**************************************************************************")
    print("Waiting for input data request:")
    print("**************************************************************************")
    print("")
    print("[INFO] Waiting for input data request at " + str(datetime.datetime.now()) + " ...")
    print("")

    # Read message wolframAlphaKnowledge_inputPort and clean
    wolframAlphaKnowledge_inputPort.read(wolframAlphaKnowledgeInputBottle)
    dataToResolve = wolframAlphaKnowledgeInputBottle.toString()
    dataToResolve = dataToResolve.replace('"','')

    print("")
    print("[RECEIVED] Data received: " + str(dataToResolve) + " at " + str(datetime.datetime.now()) + ".")
    print("")

    print("")
    print("**************************************************************************")
    print("Processing:")
    print("**************************************************************************")
    print("")

    try:
        # Sending request to Wolfram Alpha
        print("")
        print("[INFO] Connecting with Wolfram Alpha server ...")
        print("")

        serverRespone = wolframAlphaClient.query(str(dataToResolve))
        dataResolved = next(serverRespone.results).text

        print("")
        print("[INFO] Server response done.")
        print("")

        print("")
        print("**************************************************************************")
        print("Results:")
        print("**************************************************************************")
        print("")
        print("[RESULTS] Request results: " + str(dataResolved))
        print("")

    except:
        print("")
        print("[ERROR] Sorry, i couldn´t resolve your request.")
        print("")

    # Send wolframAlphaKnowledge output results
    wolframAlphaKnowledgeOutputBottle.clear()
    wolframAlphaKnowledgeOutputBottle.addString(str(dataResolved))
    wolframAlphaKnowledge_outputPort.write(wolframAlphaKnowledgeOutputBottle)

# Close YARP ports
print("[INFO] Closing YARP ports...")
wolframAlphaKnowledge_inputPort.close()
wolframAlphaKnowledge_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("wolframAlphaKnowledge program finished correctly.")
print("")
