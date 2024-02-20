import system
import argparse
import loguru

from pentestMain import pentestInit

def main():
  """ Initialize the pentest process """
  # Initialize Argument Parser to parse the command line arguments
  argumentParser = argparse.ArgumentParser(description="Argument parser to parse arguments.")

  argumentParser.add_argument(
    "--log-dir",
    type=str,
    default="logs",
    help="Path to the directory to store the session logs",
  )

  
