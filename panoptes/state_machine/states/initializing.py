from . import PanState

from ... utils import error


class State(PanState):

    def main(self):

        self.panoptes.say("Getting ready! Woohoo!")

        try:
            for cam in self.panoptes.observatory.cameras:
                cam.connect()

            self.panoptes.observatory.mount.initialize()

            if self.panoptes.observatory.mount.is_initialized:
                self.panoptes.observatory.mount.unpark()

                # We have successfully initialized so we transition to the schedule state
                self.panoptes.schedule()
            else:
                raise error.InvalidMountCommand("Mount not initialized")

        except Exception as e:
            self.panoptes.say("Oh wait. There was a problem initializing: {}".format(e))

            # Problem, transition to park state
            self.panoptes.park()
