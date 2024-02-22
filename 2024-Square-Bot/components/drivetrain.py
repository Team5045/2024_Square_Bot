import wpilib
import wpilib.drive
import wpilib.interfaces
import robotpy
import phoenix5
from phoenix5._ctre import WPI_TalonSRX
from wpimath.controller import DifferentialDriveWheelVoltages

class Drivetrain:
    talonL1: WPI_TalonSRX
    talonL2: WPI_TalonSRX
    talonR1: WPI_TalonSRX
    talonR2: WPI_TalonSRX
    control: wpilib.XboxController

    def setup(self):

        # self.l_motor = wpilib.MotorControllerGroup(self.talonL1, self.talonL2)
        # self.r_motor = wpilib.MotorControllerGroup(self.talonR1, self.talonR2)

        # self.left = wpilib.MotorControllerGroup(self.talonL1, self.talonL2)
        # self.right = wpilib.MotorControllerGroup(self.talonR1, self.talonR2)


        # self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        self.speed = 0
        self.angle = 0
        

    def execute(self):

        if abs(self.control.getLeftY()) > 0.2:
            self.speed = self.control.getLeftY()
        else:
            self.speed = 0
        if abs(self.control.getRightX()) > 0.2:
            self.angle = self.control.getRightX()
        else:
            self.angle = 0
        #self.left = self.speed * 10 
        self.left = (self.speed + self.angle) * 8#this is essentially what arcade drive is
        #self.right = self.speed * 10 
        self.right = (self.speed - self.angle) * 8 #for more info, go to 
        self.move = DifferentialDriveWheelVoltages(self.left, self.right)
        
        # self.talonL1.setVoltage()
        # self.talonL2.setVoltage()
        # self.talonR1.setVoltage()
        # self.talonR2.setVoltage()

        self.talonL1.setVoltage(output=self.move.left)
        self.talonL2.setVoltage(output=self.move.left)
        self.talonR1.setVoltage(output=-self.move.right)
        self.talonR2.setVoltage(output=self.move.right)

        # self.talonL1.setVoltage(output=self.move.left)
        # self.talonL2.setVoltage(output=self.move.left)
        # self.talonR1.setVoltage(output=self.move.right)
        # self.talonR2.setVoltage(output=self.move.right)



        
        #self.drive.arcadeDrive(self.speed, self.angle)
























#mistake code :((((
# import wpilib
# import wpilib.drive
# import wpilib.interfaces
# import phoenix6
# from phoenix6.controls.follower import Follower
# from phoenix6.hardware.talon_fx import TalonFX
# #from phoenix6.controls.differential_duty_cycle import DifferentialDutyCycle
# from phoenix6.controls.duty_cycle_out import DutyCycleOut
# from phoenix6.controls.voltage_out import VoltageOut
# import robotpy

# class Drivetrain:
#     talon_L_1: TalonFX
#     talon_L_2: TalonFX
#     talon_R_1: TalonFX
#     talon_R_2: TalonFX
#     l_request: DutyCycleOut
#     r_request: DutyCycleOut
#     _left_volts_out: VoltageOut
#     _right_volts_out: VoltageOut

#     control: wpilib.XboxController

#     def setup(self):



#         self.talon_L_2.set_control(Follower(self.talon_L_1.device_id, False))
#         self.talon_R_2.set_control(Follower(self.talon_R_1.device_id, False))




#         # self.l_request = DutyCycleOut(0.0)
#         # self.r_request = DutyCycleOut(0.0)
#         # self.R1 = wpilib.interfaces.MotorController(self.talon_R_1)
#         # self.R2 = wpilib.interfaces._interfaces.MotorController(self.talon_R_2)

#         #self.left = phoenix6.controls.differential_follower.DifferentialFollower()
#         # self.right = wpilib.MotorControllerGroup(self.talon_R_1, self.talon_R_2)


#         #self.drive = wpilib.drive.DifferentialDrive(self.talon_L_1, self.talon_R_1)

#         # speed = 0
#         # angle = 0

#         # speeds = wpilib.drive.DifferentialDrive.curvatureDriveIK(speed, angle ,True)
#         self._left_volts_out = VoltageOut(0, enable_foc=False)
#         self._right_volts_out = VoltageOut(0, enable_foc=False)

#         self.speed = 0
#         self.angle = 0

#         # speeds = wpilib.drive.DifferentialDrive.curvatureDriveIK(self.speed, self.angle ,True)

#         # self._left_volts_out.output = speeds.left * 12.0
#         # self._right_volts_out.output = speeds.right * 12.0




        
#     def execute(self):


#         if abs(self.control.getLeftY()) > 0.2:
#             self.speed = self.control.getLeftY()
#         else:
#             self.speed = 0
#         if abs(self.control.getRightX()) > 0.2:
#             self.angle = self.control.getRightX()
#         else:
#             self.angle = 0
#         speeds = wpilib.drive.DifferentialDrive.curvatureDriveIK(self.speed, self.angle ,True)

#         self._left_volts_out.output = speeds.left * 12.0
#         self._right_volts_out.output = speeds.right * 12.0



#         #left_out = self.speed + self.angle #this is essentially what arcade drive is
#         #right_out = self.speed - self.angle #for more info, go to 
#         #https://v6.docs.ctr-electronics.com/en/latest/docs/api-reference/device-specific/talonfx/open-loop-requests.html

#         # self.drive.arcadeDrive(self.speed, self.angle)

#         #speeds = wpilib.drive.DifferentialDrive.curvatureDriveIK(self.speed, self.angle, True)

#         #self.left_out = speeds.left #volts
#         #self.right_out = speeds.right

#         #self.talon_L_1.set_control(self.left_out)
#         #self.talon_R_1.set_control(self.right_out)

#         self.talon_L_1.set_control(self._left_volts_out)
#         self.talon_R_1.set_control(self._right_volts_out)
            
        