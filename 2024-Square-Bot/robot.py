
import wpilib
import wpilib.drive
import magicbot
import robotpy
import phoenix5
from phoenix5._ctre import WPI_TalonSRX
from components.drivetrain import Drivetrain

class SpartaBot(magicbot.MagicRobot):
    
    drivetrain: Drivetrain

    def createObjects(self):
        self.talonL1 = WPI_TalonSRX(12)
        self.talonL2 = WPI_TalonSRX(1)
        self.talonR1 = WPI_TalonSRX(11)
        self.talonR2 = WPI_TalonSRX(3)
        self.control = wpilib.XboxController(0)


    def teleopInit(self):
        '''Called . teleop starts; optional'''
        pass

    def teleopPeriodic(self):
        Drivetrain.execute(self)


if __name__ == '__main__':
    wpilib.run(SpartaBot)

