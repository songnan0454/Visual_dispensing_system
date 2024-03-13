import ctypes

class ZmcLibUsing:
    def __init__(self):
        self.zaux_lib = None
        self.zmotion_lib = None
        self.zaux_lib = ctypes.WinDLL('./zmc/x64/zauxdll.dll')
        self.zmotion_lib = ctypes.WinDLL('./zmc/x64/zmotion.dll')
        self.handler = ctypes.c_void_p()
        self.sim_ip = "127.0.0.1"
        self.str_ip_list = []

    def connect_to_sim(self):
        ip_bytes = self.sim_ip.encode("utf-8")
        p_ip = ctypes.c_char_p(ip_bytes)
        ret_val = self.zaux_lib.ZAux_OpenEth(p_ip, ctypes.pointer(self.handler))
        if ret_val == 0:
            print("Sim connected successfully!")
        else:
            raise Exception(f"Sim connected failed, error_code:{ret_val}")

    def aux_open_eth(self, ip_addr):
        ip_bytes = ip_addr.encode("utf-8")
        p_ip = ctypes.c_char_p(ip_bytes)
        ret_val = self.zaux_lib.ZAux_OpenEth(p_ip, ctypes.pointer(self.handler))
        if ret_val == 0:
            print("Controller connected successfully!")
        else:
            raise Exception(f"Controller connected failed, error_code:{ret_val}")

    def aux_search_eth_list(self):
        ip_list = ctypes.create_string_buffer(b'', 1024)
        self.zaux_lib.ZAux_SearchEthlist(ctypes.byref(ip_list), 1024, 200)
        self.str_ip_list = ip_list.value.decode().split()
        print(f"{len(self.str_ip_list)} controllers found!")
        return self.str_ip_list

    def aux_close(self):
        self.zaux_lib.ZAux_Close(ctypes.pointer(self.handler))

    def aux_direct_set_op(self, opt, value):
        ret_val = self.zaux_lib.ZAux_Direct_SetOp(self.handler, opt, value)
        print(f"aux_direct_set_op->ret_val:{ret_val}")

    def aux_direct_get_op(self, opt):
        pi_value = ctypes.pointer(ctypes.c_uint32(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetOp(self.handler, opt, pi_value)
        print(f"aux_direct_get_op->ret_val:{ret_val}, pi_value.contents:{pi_value.contents}")

    def get_axises(self):
        axis_num = self.zmotion_lib.ZMC_GetAxises(self.handler)
        print(f"get_axises->axis_num:{axis_num}")

    def pause(self):
        ret_val = self.zmotion_lib.ZMC_Pause(self.handler)
        print(f"pause->ret_val:{ret_val}")

    def stop(self):
        ret_val = self.zmotion_lib.ZMC_Stop(self.handler)
        print(f"stop->ret_val:{ret_val}")

    def get_in_all(self):
        pi_value = ctypes.pointer(ctypes.c_uint32(0))
        ret_val = self.zmotion_lib.ZMC_GetInAll(self.handler, 1, 16, pi_value)
        print(f"get_in_all->ret_val:{ret_val}, pi_value.contents:{pi_value.contents}")

    def get_out_all(self):
        pi_value = ctypes.pointer(ctypes.c_uint32(0))
        ret_val = self.zmotion_lib.ZMC_GetOutAll(self.handler, 1, 16, pi_value)
        print(f"get_out_all->ret_val:{ret_val}, pi_value.contents:{pi_value.contents}")

    def aux_direct_set_a_type(self, axis, axis_type):
        ret_val = self.zaux_lib.ZAux_Direct_SetAtype(self.handler, axis, axis_type)
        print(f"aux_direct_set_a_type->ret_val:{ret_val}")

    def aux_direct_get_a_type(self, axis):
        p_axis_type = ctypes.pointer(ctypes.c_uint32(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAtype(self.handler, axis, p_axis_type)
        axis_type = p_axis_type.contents
        print(f"aux_direct_get_a_type->ret_val:{ret_val}, axis_type:{axis_type}")
        return axis_type
    def aux_direct_set_units(self, axis, units):
        ret_val = self.zaux_lib.ZAux_Direct_SetUnits(self.handler, axis, ctypes.c_float(units))
        print(f"aux_direct_set_units->ret_val:{ret_val}")

    def aux_direct_get_units(self, axis):
        p_units = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetUnits(self.handler, axis, p_units)
        units = p_units.contents
        print(f"aux_direct_get_units->ret_val:{ret_val}, units:{units}")
        return units

    def aux_direct_set_speed(self, axis, speed):
        ret_val = self.zaux_lib.ZAux_Direct_SetSpeed(self.handler, axis, ctypes.c_float(speed))
        print(f"aux_direct_set_speed->ret_val:{ret_val}")

    def aux_direct_get_speed(self, axis):
        p_speed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetSpeed(self.handler, axis, p_speed)
        speed = p_speed.contents
        print(f"aux_direct_get_speed->ret_val:{ret_val}, speed:{speed}")
        return speed

    def aux_direct_set_accel(self, axis, delta_speed):
        ret_val = self.zaux_lib.ZAux_Direct_SetAccel(self.handler, axis, ctypes.c_float(delta_speed))
        print(f"aux_direct_set_accel->ret_val:{ret_val}")

    def aux_direct_get_accel(self, axis):
        p_accel = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAccel(self.handler, axis, p_accel)
        accel = p_accel.contents
        print(f"aux_direct_get_accel->ret_val:{ret_val}, accel:{accel}")
        return accel

    def aux_direct_set_decel(self, axis, delta_speed):
        ret_val = self.zaux_lib.ZAux_Direct_SetDecel(self.handler, axis, ctypes.c_float(delta_speed))
        print(f"aux_direct_set_decel->ret_val:{ret_val}")

    def aux_direct_get_decel(self, axis):
        p_decel = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetDecel(self.handler, axis, p_decel)
        decel = p_decel.contents
        print(f"aux_direct_get_decel->ret_val:{ret_val}, decel:{decel}")
        return decel

    def aux_direct_get_addax(self, axis):
        p_addax = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAddax(self.handler, axis, p_addax)
        addax = p_addax.contents
        print(f"aux_direct_get_addax->ret_val:{ret_val}, addax:{addax}")
        return addax

    def aux_direct_set_almin(self, axis, almin):
        ret_val = self.zaux_lib.ZAux_Direct_SetAlmIn(self.handler, axis, ctypes.c_int(almin))
        print(f"aux_direct_set_almin->ret_val:{ret_val}")

    def aux_direct_get_almin(self, axis):
        p_almin = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAlmIn(self.handler, axis, p_almin)
        almin = p_almin.contents
        print(f"aux_direct_get_almin->ret_val:{ret_val}, almin:{almin}")
        return almin

    def aux_direct_set_dpos(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetDpos(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_dpos->ret_val:{ret_val}")

    def aux_direct_get_dpos(self, axis):
        p_location = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetDpos(self.handler, axis, p_location)
        location = p_location.contents
        print(f"aux_direct_get_dpos->ret_val:{ret_val}, location:{location}")
        return location
    def aux_direct_set_mpos(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetMpos(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_mpos->ret_val:{ret_val}")

    def aux_direct_get_mpos(self, axis):
        p_location = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetMpos(self.handler, axis, p_location)
        location = p_location.contents
        print(f"aux_direct_get_mpos->ret_val:{ret_val}, location:{location}")
        return location

    def aux_direct_get_if_idle(self, axis):
        p_if_idle = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetIfIdle(self.handler, axis, p_if_idle)
        if_idle = p_if_idle.contents
        print(f"aux_direct_get_if_idle->ret_val:{ret_val}, if_idle:{if_idle}")
        return if_idle

    def aux_direct_get_axis_status(self, axis):
        p_status = ctypes.pointer(ctypes.c_uint32(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAxisStatus(self.handler, axis, p_status)
        status = p_status.contents
        print(f"aux_direct_get_axis_status->ret_val:{ret_val}, status:{status}")
        return status

    def aux_direct_set_axis_address(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetAxisAddress(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_axis_address->ret_val:{ret_val}")

    def aux_direct_get_axis_address(self, axis):
        p_address = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAxisAddress(self.handler, axis, p_address)
        address = p_address.contents
        print(f"aux_direct_get_axis_address->ret_val:{ret_val}, address:{address}")
        return address

    def aux_direct_set_axis_enable(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetAxisEnable(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_axis_enable->ret_val:{ret_val}")

    def aux_direct_get_axis_enable(self, axis):
        p_enable = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetAxisEnable(self.handler, axis, p_enable)
        enable = p_enable.contents
        print(f"aux_direct_get_axis_enable->ret_val:{ret_val}, enable:{enable}")
        return enable

    def aux_direct_set_clutch_rate(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetClutchRate(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_clutch_rate->ret_val:{ret_val}")

    def aux_direct_get_clutch_rate(self, axis):
        p_clutch_rate = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetClutchRate(self.handler, axis, p_clutch_rate)
        clutch_rate = p_clutch_rate.contents
        print(f"aux_direct_get_clutch_rate->ret_val:{ret_val}, clutch_rate:{clutch_rate}")
        return clutch_rate

    def aux_direct_set_close_win(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetCloseWin(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_close_win->ret_val:{ret_val}")

    def aux_direct_get_close_win(self, axis):
        p_close_win = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetCloseWin(self.handler, axis, p_close_win)
        close_win = p_close_win.contents
        print(f"aux_direct_get_close_win->ret_val:{ret_val}, close_win:{close_win}")
        return close_win

    def aux_direct_set_corner_mode(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetCornerMode(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_corner_mode->ret_val:{ret_val}")

    def aux_direct_get_corner_mode(self, axis):
        p_corner_mode = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetCornerMode(self.handler, axis, p_corner_mode)
        corner_mode = p_corner_mode.contents
        print(f"aux_direct_get_corner_mode->ret_val:{ret_val}, corner_mode:{corner_mode}")
        return corner_mode

    def aux_direct_set_creep(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetCreep(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_creep->ret_val:{ret_val}")

    def aux_direct_get_creep(self, axis):
        p_creep = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetCreep(self.handler, axis, p_creep)
        creep = p_creep.contents
        print(f"aux_direct_get_creep->ret_val:{ret_val}, creep:{creep}")
        return creep

    def aux_trigger(self):
        ret_val = self.zaux_lib.ZAux_Trigger(self.handler)
        print(f"aux_trigger->ret_val:{ret_val}")

    def aux_direct_single_move(self, axis, distance):
        ret_val = self.zaux_lib.ZAux_Direct_Single_Move(self.handler, axis, ctypes.c_float(distance))
        print(f"aux_direct_single_move->ret_val:{ret_val}")

    def aux_set_com_default_baud(self, baud_rate=38400, byte_size=8, parity=0, stop_bits=0):
        ret_val = self.zaux_lib.ZAux_SetComDefaultBaud(baud_rate, byte_size, parity, stop_bits)
        print(f"aux_set_com_default_baud->ret_val:{ret_val}")

    def aux_set_ip(self, ip_addr="192.168.0.11"):
        ip_bytes = ip_addr.encode("utf-8")
        ret_val = self.zaux_lib.ZAux_SetIp(self.handler, ctypes.c_char_p(ip_bytes))
        print(f"aux_set_ip->ret_val:{ret_val}")


    def aux_fast_open(self, type=2, connect_str="127.0.0.1", time_out=1000):
        connect_bytes = connect_str.encode("utf-8")
        ret_val = self.zaux_lib.ZAux_FastOpen(type, connect_bytes, time_out, ctypes.pointer(self.handler))
        print(f"aux_fast_open->ret_val:{ret_val}")

    def aux_get_controller_info(self):
        soft_type = ctypes.pointer(ctypes.c_char(0))
        soft_version = ctypes.pointer(ctypes.c_char(0))
        controller_id = ctypes.pointer(ctypes.c_char(0))
        ret_val = self.zaux_lib.ZAux_GetControllerInfo(self.handler, soft_type, soft_version, controller_id)
        type = soft_type.contents
        version = soft_version.contents
        id = controller_id.contents
        print(f"aux_get_controller_info->ret_val:{ret_val},type:{type},version:{version},id:{id}")

    #获取IO还有问题，待研究
    def aux_get_sys_specification(self):
        virtu_axises = ctypes.pointer(ctypes.c_int16(0))
        motors = ctypes.pointer(ctypes.c_int(0))
        c_int_array_type = ctypes.c_int * 4
        ioes = c_int_array_type(0,0,0,0)
        ret_val = self.zaux_lib.ZAux_GetSysSpecification(self.handler, virtu_axises, motors, ioes)
        axises = virtu_axises.contents
        motor_num = motors.contents
        for item in ioes:
            print(f"aux_get_controller_info->ioes:{item}")
        print(f"aux_get_controller_info->ret_val:{ret_val},axises:{axises},motor_num:{motor_num}")

if __name__ == "__main__":
    test_obj = ZmcLibUsing()
    test_obj.connect_to_sim()
    """
    test_obj.aux_set_com_default_baud()
    test_obj.aux_direct_set_a_type(0, 1)
    test_obj.aux_direct_get_a_type(0)
    test_obj.aux_direct_set_units(0, 100)
    test_obj.aux_direct_get_units(0)
    test_obj.aux_direct_set_speed(0, 200)
    test_obj.aux_direct_get_speed(0)
    test_obj.aux_direct_set_accel(0, 2000)
    test_obj.aux_direct_get_accel(0)
    test_obj.aux_direct_set_decel(0, 2000)
    test_obj.aux_direct_get_decel(0)
    test_obj.aux_direct_set_dpos(0, 0)
    test_obj.aux_direct_get_dpos(0)
    test_obj.aux_direct_set_mpos(0, 0)
    test_obj.aux_direct_get_mpos(0)
    test_obj.aux_trigger()
    test_obj.aux_direct_single_move(0, 500)
    test_obj.aux_direct_get_if_idle(0)
    test_obj.aux_direct_get_axis_status(0)
    test_obj.aux_set_ip()
    test_obj.aux_fast_open()
    """
    test_obj.aux_get_controller_info()
    test_obj.aux_get_sys_specification()
