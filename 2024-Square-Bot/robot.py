
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







#i hate life
# import wpilib
# import wpilib.drive
# import magicbot
# import phoenix6
# from phoenix6.hardware.talon_fx import TalonFX
# import phoenix6.hardware.core.core_talon_fx as talon
# import phoenix6.hardware.core as talon
# from components.drivetrain import Drivetrain
# from phoenix6.controls.duty_cycle_out import DutyCycleOut
# from phoenix6.controls.voltage_out import VoltageOut

#class SpartaBot(magicbot.MagicRobot):

#     drivetrain: Drivetrain

#     def createObjects(self):
#         '''Create motors and stuff here'''
#         self.control = wpilib.XboxController(0)

#         self.talon_L_1 = TalonFX(11)
#         #self.talon_L_2 = talon.oreTalonFX(2)
#         self.talon_L_2 = TalonFX(1)
#         self.talon_R_1 = TalonFX(12)
#         #self.talon_R_2 = talon.CoreTalonFX(4)
#         self.talon_R_2 = TalonFX(3)

#         self.l_request = DutyCycleOut(0.0)
#         self.r_request = DutyCycleOut(0.0)

#         self._left_volts_out = VoltageOut(0, enable_foc=False)
#         self._right_volts_out = VoltageOut(0, enable_foc=False)

#     def teleopInit(self):
#         '''Called . teleop starts; optional'''
#         pass

#     def teleopPeriodic(self):
#         Drivetrain.execute(self)


# if __name__ == '__main__':
#     wpilib.run(SpartaBot)