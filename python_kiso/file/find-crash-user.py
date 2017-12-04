#1 Find line of OUTLOOK.EXE error event
#   - Store the event into lines
#2 Get an affected hostname
#3 Find other line using the same hostname
#   - If a line is found, store the event into lines
#   - If a line is not found nearby the error event, store line with following format
#       1st column: Time(same as the erro event)
#       the rest: NOT found
#4 If reading reachs the end of lines, stored lines will output as "find-crash-user_XXXXXX.csv"
import pandas as pd
import sys


#####################
# Main

args = sys.argv
df = pd.read_csv("args[1]")
