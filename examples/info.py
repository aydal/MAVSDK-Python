import datetime
import json
import asyncio
import time
from mavsdk import start_mavlink
from mavsdk import connect as mavsdk_connect

async def print_battery():
    global volt,batt
    async for battery in drone.telemetry.battery():
        volt=battery.voltage_v
        batt=battery.remaining_percent

async def print_gps_info():
    global satnum,fixt
    async for g in drone.telemetry.gps_info():
        satnum=g.num_satellites
        fixt=str(g.fix_type)

async def print_armed():
    global armed
    async for arm in drone.telemetry.armed():
        armed=arm


async def print_position():
    global lat,lon,abs_ht,rel_ht
    async for p in drone.telemetry.position():
        lat=p.latitude_deg
        lon=p.longitude_deg
        abs_ht=p.absolute_altitude_m
        rel_ht=p.relative_altitude_m

async def print_state():
    global uuid,is_con
    async for state in drone.core.connection_state():
        uuid=state.uuid
        is_con=state.is_connected

async def print_mode():
    global mode
    async for f in drone.telemetry.flight_mode():
        mode=str(f)

async def print_att():
    global roll, pitch, yaw
    async for a in drone.telemetry.attitude_euler():
        roll=a.roll_deg
        pitch=a.pitch_deg 
        yaw=a.yaw_deg

async def print_speed():
    global vnorth, veast, vdown
    async for v in drone.telemetry.ground_speed_ned():
        vnorth=v.velocity_north_m_s
        veast=v.velocity_east_m_s
        vdown=v.velocity_down_m_s

'''async def print_home():
    global home_lat, home_lon, home_abs, home_rel
    async for h in drone.telemetry.home():
        home_lat=h.latitude_deg
        home_lon=h.longitude_deg
        home_abs=h.absolute_altitude_m
        home_rel=h.relative_altitude_m'''


async def publish_value():
    global uuid,is_con,volt,batt,armed,mode,satnum,fixt,lat,lon,abs_ht,rel_ht, roll, pitch, yaw, home_lat, home_lon, home_abs, vnorth, veast, vdown
    while True:
        print( json.dumps({  "timestamp" : str(datetime.datetime.now()),
        "connection_state" : is_con,
        "uuid" : uuid,
        "battery" : {"voltage" : volt, "remaining_percent": batt},
        "arm_status" : armed,
        "flight_mode" : mode,
        "gps_info" : { "satellite_number" : satnum, "fix_type" : fixt},
        "position" : {"lat":lat, "lon":lon, "abs_ht":abs_ht, "rel_ht":rel_ht},
        "home": {"lat":home_lat, "lon":home_lon, "abs_ht": home_abs },
        "speed": {"north":vnorth, "east":veast, "down":vdown},
        "attitude":{"roll":roll, "pitch":pitch, "yaw":yaw} }))
        await asyncio.sleep(0.2)

def setup_tasks():
    # Create asyncio tasks with the default eventloop
    # asyncio.create_task() is only callable when the event loop is already
    # running!!!
    asyncio.ensure_future(print_position())
    asyncio.ensure_future(print_speed())    
    asyncio.ensure_future(print_battery())
    asyncio.ensure_future(print_mode())
    asyncio.ensure_future(print_armed())
    asyncio.ensure_future(print_state())
    asyncio.ensure_future(print_att())
    asyncio.ensure_future(print_gps_info())
    #asyncio.ensure_future(print_home())

    #Publishing
    asyncio.ensure_future(publish_value())

async def initialise():
    global drone

    async for state in drone.core.connection_state():
        break

    async for battery in drone.telemetry.battery():
        break
    
    async for arm in drone.telemetry.armed(): 
        break
    
    async for f in drone.telemetry.flight_mode():
        break
    
    async for g in drone.telemetry.gps_info():
        break

    async for p in drone.telemetry.position():
        break

    async for a in drone.telemetry.attitude_euler():
        break

    async for h in drone.telemetry.home():
        break

    async for v in drone.telemetry.ground_speed_ned():
        break

    return(state.uuid, state.is_connected, battery.voltage_v, battery.remaining_percent, arm, str(f), g.num_satellites, str(g.fix_type), p.latitude_deg,
        p.longitude_deg, p.absolute_altitude_m, p.relative_altitude_m, a.roll_deg, a.pitch_deg, a.yaw_deg, h.latitude_deg, h.longitude_deg, 
        h.absolute_altitude_m, v.velocity_north_m_s, v.velocity_east_m_s, v.velocity_down_m_s)

def telval():
    return asyncio.get_event_loop().run_until_complete(initialise())


# Read in command-line parameters

start_mavlink()
drone = mavsdk_connect(host="127.0.0.1")
print("Waiting for drone...")
(uuid,is_con,volt,batt,armed,mode,satnum,fixt,lat,lon,abs_ht,rel_ht, roll, pitch, yaw, home_lat, home_lon, home_abs, vnorth, veast, vdown) = telval()
#x = threading.Thread(target=termprint, daemon=True)
#x.start()

setup_tasks()
asyncio.get_event_loop().run_forever()



