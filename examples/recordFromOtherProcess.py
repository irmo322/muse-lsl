import time
from pathlib import Path

from muselsl.record import Recorder


_HERE = Path(__file__).parent


if __name__ == "__main__":

    print("Creating Recorder")
    recorder = Recorder(filename=_HERE / "record_from_other_process.csv", verbose=True)

    print("Starting Recorder and waiting for 30 seconds...")
    time.sleep(1)
    recorder.start_record()

    time.sleep(30)

    print("Stopping Recorder")
    time.sleep(1)
    recorder.end_record()

    print("End of script")
