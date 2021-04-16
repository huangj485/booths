import argparse
import booths
 
 
# Initialize parser
parser = argparse.ArgumentParser(description = "Multiply A and B with Booth's Algorithm")

# Define args
parser.add_argument("-A", type=int, required=True, help = "multiplicand")
parser.add_argument("-B", type=int, required=True, help = "multiplier")
parser.add_argument("--s", dest = "s", action='store_true', help = "flag to save instead of print to console")
 
# Read args
args = parser.parse_args()
A = args.A #multiplicand
B = args.B #multiplier

value = booths.mul(A, B)

if args.s:
  f = open("saved.txt", "w")
  f.write(value)
  f.close()
else:
  print(value)
