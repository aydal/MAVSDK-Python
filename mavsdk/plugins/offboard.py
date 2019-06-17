# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import offboard_pb2, offboard_pb2_grpc
from enum import Enum


class Attitude:
    """ Generated by dcsdkgen """

    

    def __init__(
            self,
            roll_deg,
            pitch_deg,
            yaw_deg,
            thrust_value):
        """ Initializes the Attitude object """
        self.roll_deg = roll_deg
        self.pitch_deg = pitch_deg
        self.yaw_deg = yaw_deg
        self.thrust_value = thrust_value

    def __equals__(self, to_compare):
        """ Checks if two Attitude are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Attitude object
            return \
                (self.roll_deg == to_compare.roll_deg) and \
                (self.pitch_deg == to_compare.pitch_deg) and \
                (self.yaw_deg == to_compare.yaw_deg) and \
                (self.thrust_value == to_compare.thrust_value)

        except AttributeError:
            return False

    def __str__(self):
        """ Attitude in string representation """
        struct_repr = ", ".join([
                "roll_deg: " + str(self.roll_deg),
                "pitch_deg: " + str(self.pitch_deg),
                "yaw_deg: " + str(self.yaw_deg),
                "thrust_value: " + str(self.thrust_value)
                ])

        return f"Attitude: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAttitude):
        """ Translates a gRPC struct to the SDK equivalent """
        return Attitude(
                
                rpcAttitude.roll_deg,
                
                
                rpcAttitude.pitch_deg,
                
                
                rpcAttitude.yaw_deg,
                
                
                rpcAttitude.thrust_value
                )

    def translate_to_rpc(self, rpcAttitude):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAttitude.roll_deg = self.roll_deg
            
        
        
        
            
        rpcAttitude.pitch_deg = self.pitch_deg
            
        
        
        
            
        rpcAttitude.yaw_deg = self.yaw_deg
            
        
        
        
            
        rpcAttitude.thrust_value = self.thrust_value
            
        
        


class AttitudeRate:
    """ Generated by dcsdkgen """

    

    def __init__(
            self,
            roll_deg_s,
            pitch_deg_s,
            yaw_deg_s,
            thrust_value):
        """ Initializes the AttitudeRate object """
        self.roll_deg_s = roll_deg_s
        self.pitch_deg_s = pitch_deg_s
        self.yaw_deg_s = yaw_deg_s
        self.thrust_value = thrust_value

    def __equals__(self, to_compare):
        """ Checks if two AttitudeRate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AttitudeRate object
            return \
                (self.roll_deg_s == to_compare.roll_deg_s) and \
                (self.pitch_deg_s == to_compare.pitch_deg_s) and \
                (self.yaw_deg_s == to_compare.yaw_deg_s) and \
                (self.thrust_value == to_compare.thrust_value)

        except AttributeError:
            return False

    def __str__(self):
        """ AttitudeRate in string representation """
        struct_repr = ", ".join([
                "roll_deg_s: " + str(self.roll_deg_s),
                "pitch_deg_s: " + str(self.pitch_deg_s),
                "yaw_deg_s: " + str(self.yaw_deg_s),
                "thrust_value: " + str(self.thrust_value)
                ])

        return f"AttitudeRate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAttitudeRate):
        """ Translates a gRPC struct to the SDK equivalent """
        return AttitudeRate(
                
                rpcAttitudeRate.roll_deg_s,
                
                
                rpcAttitudeRate.pitch_deg_s,
                
                
                rpcAttitudeRate.yaw_deg_s,
                
                
                rpcAttitudeRate.thrust_value
                )

    def translate_to_rpc(self, rpcAttitudeRate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAttitudeRate.roll_deg_s = self.roll_deg_s
            
        
        
        
            
        rpcAttitudeRate.pitch_deg_s = self.pitch_deg_s
            
        
        
        
            
        rpcAttitudeRate.yaw_deg_s = self.yaw_deg_s
            
        
        
        
            
        rpcAttitudeRate.thrust_value = self.thrust_value
            
        
        


class PositionNEDYaw:
    """ Generated by dcsdkgen """

    

    def __init__(
            self,
            north_m,
            east_m,
            down_m,
            yaw_deg):
        """ Initializes the PositionNEDYaw object """
        self.north_m = north_m
        self.east_m = east_m
        self.down_m = down_m
        self.yaw_deg = yaw_deg

    def __equals__(self, to_compare):
        """ Checks if two PositionNEDYaw are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PositionNEDYaw object
            return \
                (self.north_m == to_compare.north_m) and \
                (self.east_m == to_compare.east_m) and \
                (self.down_m == to_compare.down_m) and \
                (self.yaw_deg == to_compare.yaw_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ PositionNEDYaw in string representation """
        struct_repr = ", ".join([
                "north_m: " + str(self.north_m),
                "east_m: " + str(self.east_m),
                "down_m: " + str(self.down_m),
                "yaw_deg: " + str(self.yaw_deg)
                ])

        return f"PositionNEDYaw: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPositionNEDYaw):
        """ Translates a gRPC struct to the SDK equivalent """
        return PositionNEDYaw(
                
                rpcPositionNEDYaw.north_m,
                
                
                rpcPositionNEDYaw.east_m,
                
                
                rpcPositionNEDYaw.down_m,
                
                
                rpcPositionNEDYaw.yaw_deg
                )

    def translate_to_rpc(self, rpcPositionNEDYaw):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPositionNEDYaw.north_m = self.north_m
            
        
        
        
            
        rpcPositionNEDYaw.east_m = self.east_m
            
        
        
        
            
        rpcPositionNEDYaw.down_m = self.down_m
            
        
        
        
            
        rpcPositionNEDYaw.yaw_deg = self.yaw_deg
            
        
        


class VelocityBodyYawspeed:
    """ Generated by dcsdkgen """

    

    def __init__(
            self,
            forward_m_s,
            right_m_s,
            down_m_s,
            yawspeed_deg_s):
        """ Initializes the VelocityBodyYawspeed object """
        self.forward_m_s = forward_m_s
        self.right_m_s = right_m_s
        self.down_m_s = down_m_s
        self.yawspeed_deg_s = yawspeed_deg_s

    def __equals__(self, to_compare):
        """ Checks if two VelocityBodyYawspeed are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VelocityBodyYawspeed object
            return \
                (self.forward_m_s == to_compare.forward_m_s) and \
                (self.right_m_s == to_compare.right_m_s) and \
                (self.down_m_s == to_compare.down_m_s) and \
                (self.yawspeed_deg_s == to_compare.yawspeed_deg_s)

        except AttributeError:
            return False

    def __str__(self):
        """ VelocityBodyYawspeed in string representation """
        struct_repr = ", ".join([
                "forward_m_s: " + str(self.forward_m_s),
                "right_m_s: " + str(self.right_m_s),
                "down_m_s: " + str(self.down_m_s),
                "yawspeed_deg_s: " + str(self.yawspeed_deg_s)
                ])

        return f"VelocityBodyYawspeed: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVelocityBodyYawspeed):
        """ Translates a gRPC struct to the SDK equivalent """
        return VelocityBodyYawspeed(
                
                rpcVelocityBodyYawspeed.forward_m_s,
                
                
                rpcVelocityBodyYawspeed.right_m_s,
                
                
                rpcVelocityBodyYawspeed.down_m_s,
                
                
                rpcVelocityBodyYawspeed.yawspeed_deg_s
                )

    def translate_to_rpc(self, rpcVelocityBodyYawspeed):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVelocityBodyYawspeed.forward_m_s = self.forward_m_s
            
        
        
        
            
        rpcVelocityBodyYawspeed.right_m_s = self.right_m_s
            
        
        
        
            
        rpcVelocityBodyYawspeed.down_m_s = self.down_m_s
            
        
        
        
            
        rpcVelocityBodyYawspeed.yawspeed_deg_s = self.yawspeed_deg_s
            
        
        


class VelocityNEDYaw:
    """ Generated by dcsdkgen """

    

    def __init__(
            self,
            north_m_s,
            east_m_s,
            down_m_s,
            yaw_deg):
        """ Initializes the VelocityNEDYaw object """
        self.north_m_s = north_m_s
        self.east_m_s = east_m_s
        self.down_m_s = down_m_s
        self.yaw_deg = yaw_deg

    def __equals__(self, to_compare):
        """ Checks if two VelocityNEDYaw are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VelocityNEDYaw object
            return \
                (self.north_m_s == to_compare.north_m_s) and \
                (self.east_m_s == to_compare.east_m_s) and \
                (self.down_m_s == to_compare.down_m_s) and \
                (self.yaw_deg == to_compare.yaw_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ VelocityNEDYaw in string representation """
        struct_repr = ", ".join([
                "north_m_s: " + str(self.north_m_s),
                "east_m_s: " + str(self.east_m_s),
                "down_m_s: " + str(self.down_m_s),
                "yaw_deg: " + str(self.yaw_deg)
                ])

        return f"VelocityNEDYaw: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVelocityNEDYaw):
        """ Translates a gRPC struct to the SDK equivalent """
        return VelocityNEDYaw(
                
                rpcVelocityNEDYaw.north_m_s,
                
                
                rpcVelocityNEDYaw.east_m_s,
                
                
                rpcVelocityNEDYaw.down_m_s,
                
                
                rpcVelocityNEDYaw.yaw_deg
                )

    def translate_to_rpc(self, rpcVelocityNEDYaw):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVelocityNEDYaw.north_m_s = self.north_m_s
            
        
        
        
            
        rpcVelocityNEDYaw.east_m_s = self.east_m_s
            
        
        
        
            
        rpcVelocityNEDYaw.down_m_s = self.down_m_s
            
        
        
        
            
        rpcVelocityNEDYaw.yaw_deg = self.yaw_deg
            
        
        


class OffboardResult:
    """ Generated by dcsdkgen """

    
    
    class Result(Enum):
        """ Generated by dcsdkgen """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6
        NO_SETPOINT_SET = 7

        def translate_to_rpc(self, rpcResult):
            rpcResult = {
                    0: offboard_pb2.OffboardResult.UNKNOWN,
                    1: offboard_pb2.OffboardResult.SUCCESS,
                    2: offboard_pb2.OffboardResult.NO_SYSTEM,
                    3: offboard_pb2.OffboardResult.CONNECTION_ERROR,
                    4: offboard_pb2.OffboardResult.BUSY,
                    5: offboard_pb2.OffboardResult.COMMAND_DENIED,
                    6: offboard_pb2.OffboardResult.TIMEOUT,
                    7: offboard_pb2.OffboardResult.NO_SETPOINT_SET
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: OffboardResult.Result.UNKNOWN,
                    1: OffboardResult.Result.SUCCESS,
                    2: OffboardResult.Result.NO_SYSTEM,
                    3: OffboardResult.Result.CONNECTION_ERROR,
                    4: OffboardResult.Result.BUSY,
                    5: OffboardResult.Result.COMMAND_DENIED,
                    6: OffboardResult.Result.TIMEOUT,
                    7: OffboardResult.Result.NO_SETPOINT_SET,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the OffboardResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two OffboardResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # OffboardResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ OffboardResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"OffboardResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcOffboardResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return OffboardResult(
                
                OffboardResult.Result.translate_from_rpc(rpcOffboardResult.result),
                
                
                rpcOffboardResult.result_str
                )

    def translate_to_rpc(self, rpcOffboardResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.result.translate_to_rpc(rpcOffboardResult.result)
            
        
        
        
            
        rpcOffboardResult.result_str = self.result_str
            
        
        



class OffboardError(Exception):
    """ Raised when a OffboardResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Offboard(AsyncBase):
    """ Generated by dcsdkgen - MAVSDK Offboard API """

    # Plugin name
    name = "Offboard"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = offboard_pb2_grpc.OffboardServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return OffboardResult.translate_from_rpc(response.offboard_result)
    

    async def start(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.StartRequest()
        response = await self._stub.Start(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "start()")
        

    async def stop(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.StopRequest()
        response = await self._stub.Stop(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "stop()")
        

    async def is_active(self):
        """ Generated by dcsdkgen

        :returns: requested value
        """

        request = offboard_pb2.IsActiveRequest()
        response = await self._stub.IsActive(request)

        

        return response.is_active
        

    async def set_attitude(self, attitude):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.SetAttitudeRequest()
        
        attitude.translate_to_rpc(request.attitude)
                
            
        response = await self._stub.SetAttitude(request)

        

    async def set_attitude_rate(self, attitude_rate):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.SetAttitudeRateRequest()
        
        attitude_rate.translate_to_rpc(request.attitude_rate)
                
            
        response = await self._stub.SetAttitudeRate(request)

        

    async def set_position_ned(self, position_ned_yaw):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.SetPositionNedRequest()
        
        position_ned_yaw.translate_to_rpc(request.position_ned_yaw)
                
            
        response = await self._stub.SetPositionNed(request)

        

    async def set_velocity_body(self, velocity_body_yawspeed):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.SetVelocityBodyRequest()
        
        velocity_body_yawspeed.translate_to_rpc(request.velocity_body_yawspeed)
                
            
        response = await self._stub.SetVelocityBody(request)

        

    async def set_velocity_ned(self, velocity_ned_yaw):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = offboard_pb2.SetVelocityNedRequest()
        
        velocity_ned_yaw.translate_to_rpc(request.velocity_ned_yaw)
                
            
        response = await self._stub.SetVelocityNed(request)

        