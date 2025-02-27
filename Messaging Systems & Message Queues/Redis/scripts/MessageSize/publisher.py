#!/usr/bin/python3

import sys

from redisapi.redisclients import RedisPublisher



MESSAGE_DIR="/home/vagrant/FinalProject/DesignOfExperiments/messages/"
MESSAGE_SUFFIX = ".txt"

messages = [
    'tiny',
    "small",
    "medium",
    "large",
    "xlarge"
]


print("Make sure that your subscriber is already running and subscribed to the appropriate channel.")

def main():
    loops = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    file = sys.argv[2] if len(sys.argv) > 2 else "tiny"
    if file not in messages:
        print("File must be in [tiny, small, medium, large, xlarge]. Using {}.".format(messages[0]))
        file = messages[0]
        
    publisher = RedisPublisher()

    filename = MESSAGE_DIR + file + MESSAGE_SUFFIX
    
    with open(filename, "r") as f:
        data = f.read()
        
    run(publisher, data, loops)
    
def run(publisher, data, loops):
    count = 0
    for i in range(loops):
        publisher.publish(data)
        
if __name__ == '__main__':
    main()
