'''
 * ************************************************************
 *      Program: Wolfram Alpha Knowledge
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */

/*
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
print("Starting system...")

print("")
print("Loading Wolfram Alpha Knowledge engine...")

print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network...")

# Init YARP Network
yarp.Network.init()


print("")
print("Opening data input port with name /wolframAlphaKnowledge/data:i ...")

# Open input data port
wolframAlphaKnowledge_inputPort = yarp.Port()
wolframAlphaKnowledge_inputPortName = '/wolframAlphaKnowledge/data:i'
wolframAlphaKnowledge_inputPort.open(wolframAlphaKnowledge_inputPortName)

# Create input data bottle
inputBottle=yarp.Bottle()

print("")
print("Opening data output port with name /wolframAlphaKnowledge/data:o ...")

# Open output data port
wolframAlphaKnowledge_outputPort = yarp.Port()
wolframAlphaKnowledge_outputPortName = '/wolframAlphaKnowledge/data:o'
wolframAlphaKnowledge_outputPort.open(wolframAlphaKnowledge_outputPortName)

# Create output data bottle
outputBottle=yarp.Bottle()


print("")
print("Initializing wolframAlphaKnowledge engine...")

# Get system configuration
print("")
print("Detecting system and release version...")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("")
print("**************************************************************************")
print("Authentication:")
print("**************************************************************************")

# Get autentication data
print("")
print("Getting authentication data ...")
authenticationObject = configparser.ConfigParser()
authenticationObject.read('../config/authentication.ini')
authenticationObject.sections()

userID = authenticationObject['Authentication']['user-id']
accessToken = authenticationObject['Authentication']['access-token']

print("Data obtained correctly.")
print("")
print("Selected user: "+ str(userID))

print("")
print("")
print("**************************************************************************")
print("Wolfram Alpha client:")
print("**************************************************************************")
print("")
print("Configuring Wolfram Alpha authentication client ...")

wolframAlphaClient = wolframalpha.Client(str(accessToken))

print("Client configuration done.")


while True:

    # Waiting to input data
    print("")
    print("Waiting for input data ...")

    wolframAlphaKnowledge_inputPort.read(inputBottle)
    dataToResolve = inputBottle.toString()
    dataToResolve = dataToResolve.replace('"','')

    print("Data received: "+str(dataToResolve))

    print("")
    print("")
    print("**************************************************************************")
    print("Processing:")
    print("**************************************************************************")

    try:
        # Sending request to Wolfram Alpha
        print("")
        print("Connecting with Wolfram Alpha server ...")
        serverRespone = wolframAlphaClient.query(str(dataToResolve))
        dataResolved = next(serverRespone.results).text
        print("")
        print("Server response done.")

        print("")
        print("")
        print("**************************************************************************")
        print("Results:")
        print("**************************************************************************")
        print("")
        print(dataResolved)
    except:
        print("")
        print("Sorry, i could´t resolve your request.")


    # Send output results
    outputBottle.clear()
    outputBottle.addString(str(dataResolved))
    wolframAlphaKnowledge_outputPort.write(outputBottle)

# Close YARP ports
print("Closing YARP ports...")
wolframAlphaKnowledge_inputPort.close()
wolframAlphaKnowledge_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
