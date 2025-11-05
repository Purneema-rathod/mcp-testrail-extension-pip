import argparse
from .server import mcp

def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()
