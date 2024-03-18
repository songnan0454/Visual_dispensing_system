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

    def aux_direct_set_datumin(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetDatumIn(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_datumin->ret_val:{ret_val}")

    def aux_direct_get_datumin(self, axis):
        p_datumin = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.ZAux_Direct_GetDatumIn(self.handler, axis, p_datumin)
        datumin = p_datumin.contents
        print(f"aux_direct_get_datumin->ret_val:{ret_val}, datumin:{datumin}")
        return datumin

    def aux_direct_set_decel_angle(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetDecelAngle(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_decel_angle->ret_val:{ret_val}")

    def aux_direct_get_decel_angle(self, axis):
        p_decel_angle = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetDecelAngle(self.handler, axis, p_decel_angle)
        decel_angle = p_decel_angle.contents
        print(f"aux_direct_get_decel_angle->ret_val:{ret_val}, decel_angle:{decel_angle}")
        return decel_angle

    def aux_direct_get_encoder(self, axis):
        p_encoder = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetEncoder(self.handler, axis, p_encoder)
        encoder = p_encoder.contents
        print(f"aux_direct_get_encoder->ret_val:{ret_val}, encoder:{encoder}")
        return encoder

    def aux_direct_get_end_move(self, axis):
        p_end_move = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetEndMove(self.handler, axis, p_end_move)
        encoder = p_end_move.contents
        print(f"aux_direct_get_end_move->ret_val:{ret_val}, encoder:{encoder}")
        return encoder

    def aux_direct_get_end_move_buffer(self, axis):
        p_end_move_buffer = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetEndMoveBuffer(self.handler, axis, p_end_move_buffer)
        end_move_buffer = p_end_move_buffer.contents
        print(f"aux_direct_get_end_move_buffer->ret_val:{ret_val}, end_move_buffer:{end_move_buffer}")
        return end_move_buffer

    def aux_direct_set_end_move_speed(self, axis, location):
        ret_val = self.zaux_lib.ZAux_Direct_SetEndMoveSpeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_end_move_speed->ret_val:{ret_val}")

    def aux_direct_get_end_move_speed(self, axis):
        p_end_move_speed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.ZAux_Direct_GetEndMoveSpeed(self.handler, axis, p_end_move_speed)
        end_move_speed = p_end_move_speed.contents
        print(f"aux_direct_get_end_move_speed->ret_val:{ret_val}, end_move_speed:{end_move_speed}")
        return end_move_speed

    def aux_direct_set_da(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_DA(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_da->ret_val:{ret_val}")


    def aux_direct_set_invertin(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_InvertIn(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_invertin->ret_val:{ret_val}")


    def aux_direct_set_pwmfreq(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_PwmFreq(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_pwmfreq->ret_val:{ret_val}")


    def aux_direct_set_pwmduty(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_PwmDuty(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_pwmduty->ret_val:{ret_val}")

    def aux_direct_set_atype(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Atype(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_atype->ret_val:{ret_val}")

    def aux_direct_set_axisaddress(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_AxisAddress(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_axisaddress->ret_val:{ret_val}")

    def aux_direct_set_axisenable(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_AxisEnable(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_axisenable->ret_val:{ret_val}")

    def aux_direct_set_clutchrate(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_ClutchRate(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_clutchrate->ret_val:{ret_val}")

    def aux_direct_set_closewin(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_CloseWin(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_closewin->ret_val:{ret_val}")

    def aux_direct_set_cornermode(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_CornerMode(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_cornermode->ret_val:{ret_val}")

    def aux_direct_set_decelangle(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_DecelAngle(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_decelangle->ret_val:{ret_val}")

    def aux_direct_set_endmovespeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_EndMoveSpeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_endmovespeed->ret_val:{ret_val}")

    def aux_direct_set_errormask(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Errormask(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_errormask->ret_val:{ret_val}")

    def aux_direct_set_fastjog(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FastJog(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_fastjog->ret_val:{ret_val}")

    def aux_direct_set_fastdec(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FastDec(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_fastdec->ret_val:{ret_val}")

    def aux_direct_set_felimit(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FeLimit(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_felimit->ret_val:{ret_val}")

    def aux_direct_set_frange(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FRange(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_frange->ret_val:{ret_val}")

    def aux_direct_set_fholdin(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FholdIn(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_fholdin->ret_val:{ret_val}")

    def aux_direct_set_fhspeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Fhspeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_fhspeed->ret_val:{ret_val}")

    def aux_direct_set_forcespeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_ForceSpeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_forcespeed->ret_val:{ret_val}")

    def aux_direct_set_fslimit(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FsLimit(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_fslimit->ret_val:{ret_val}")

    def aux_direct_set_fullspradius(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FullSpRadius(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_fullspradius->ret_val:{ret_val}")

    def aux_direct_set_fwdin(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FwdIn(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_fwdin->ret_val:{ret_val}")

    def aux_direct_set_fwdjog(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_FwdJog(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_fwdjog->ret_val:{ret_val}")

    def aux_direct_set_invertstep(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_InvertStep(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_invertstep->ret_val:{ret_val}")

    def aux_direct_set_interpfactor(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_InterpFactor(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_interpfactor->ret_val:{ret_val}")

    def aux_direct_set_jogspeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_JogSpeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_jogspeed->ret_val:{ret_val}")

    def aux_direct_set_lspeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Lspeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_lspeed->ret_val:{ret_val}")

    def aux_direct_set_homewait(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_HomeWait(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_homewait->ret_val:{ret_val}")

    def aux_direct_set_maxspeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_MaxSpeed(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_maxspeed->ret_val:{ret_val}")

    def aux_direct_set_merge(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Merge(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_merge->ret_val:{ret_val}")

    def aux_direct_set_movemark(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Movemark(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_movemark->ret_val:{ret_val}")

    def aux_direct_set_offpos(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Offpos(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_offpos->ret_val:{ret_val}")

    def aux_direct_set_openwin(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_OpenWin(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_openwin->ret_val:{ret_val}")

    def aux_direct_set_repdist(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_RepDist(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_repdist->ret_val:{ret_val}")

    def aux_direct_set_repoption(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_RepOption(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_repoption->ret_val:{ret_val}")

    def aux_direct_set_revin(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_RevIn(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_revin->ret_val:{ret_val}")

    def aux_direct_set_revjog(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_RevJog(self.handler, axis, ctypes.c_int(location))
        print(f"aux_direct_set_revjog->ret_val:{ret_val}")

    def aux_direct_set_rslimit(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_RsLimit(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_rslimit->ret_val:{ret_val}")

    def aux_direct_set_sramp(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_Sramp(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_sramp->ret_val:{ret_val}")

    def aux_direct_set_startmovespeed(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_StartMoveSpeed(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_startmovespeed->ret_val:{ret_val}")

    def aux_direct_set_stopangle(self, axis, location):
        ret_val = self.zaux_lib.Zaux_direct_set_StopAngle(self.handler, axis, ctypes.c_float(location))
        print(f"aux_direct_set_stopangle->ret_val:{ret_val}")

    def aux_direct_getad(self, axis):
        p_ad = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_AD(self.handler, axis, p_ad)
        value = p_ad.contents
        print(f"function_name->ret_val:{ret_val}, ad:{value}")
        return value

    def aux_direct_get_da(self, axis):
        p_da = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_DA(self.handler, axis, p_da)
        value = p_da.contents
        print(f"function_name->ret_val:{ret_val}, da:{value}")
        return value

    def aux_direct_get_invertin(self, axis):
        p_invertin = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_InvertIn(self.handler, axis, p_invertin)
        value = p_invertin.contents
        print(f"function_name->ret_val:{ret_val}, invertin:{value}")
        return value

    def aux_direct_get_pwmfreq(self, axis):
        p_pwmfreq = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_PwmFreq(self.handler, axis, p_pwmfreq)
        value = p_pwmfreq.contents
        print(f"function_name->ret_val:{ret_val}, pwmfreq:{value}")
        return value

    def aux_direct_get_pwmduty(self, axis):
        p_pwmduty = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_PwmDuty(self.handler, axis, p_pwmduty)
        value = p_pwmduty.contents
        print(f"function_name->ret_val:{ret_val}, pwmduty:{value}")
        return value

    def aux_direct_get_atype(self, axis):
        p_atype = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Atype(self.handler, axis, p_atype)
        value = p_atype.contents
        print(f"function_name->ret_val:{ret_val}, atype:{value}")
        return value

    def aux_direct_get_axisstatus(self, axis):
        p_axisstatus = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_AxisStatus(self.handler, axis, p_axisstatus)
        value = p_axisstatus.contents
        print(f"function_name->ret_val:{ret_val}, axisstatus:{value}")
        return value

    def aux_direct_get_axisaddress(self, axis):
        p_axisaddress = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_AxisAddress(self.handler, axis, p_axisaddress)
        value = p_axisaddress.contents
        print(f"function_name->ret_val:{ret_val}, axisaddress:{value}")
        return value

    def aux_direct_get_axisenable(self, axis):
        p_axisenable = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_AxisEnable(self.handler, axis, p_axisenable)
        value = p_axisenable.contents
        print(f"function_name->ret_val:{ret_val}, axisenable:{value}")
        return value

    def aux_direct_get_clutchrate(self, axis):
        p_clutchrate = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_ClutchRate(self.handler, axis, p_clutchrate)
        value = p_clutchrate.contents
        print(f"function_name->ret_val:{ret_val}, clutchrate:{value}")
        return value

    def aux_direct_get_closewin(self, axis):
        p_closewin = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_CloseWin(self.handler, axis, p_closewin)
        value = p_closewin.contents
        print(f"function_name->ret_val:{ret_val}, closewin:{value}")
        return value

    def aux_direct_get_cornermode(self, axis):
        p_cornermode = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_CornerMode(self.handler, axis, p_cornermode)
        value = p_cornermode.contents
        print(f"function_name->ret_val:{ret_val}, cornermode:{value}")
        return value

    def aux_direct_get_decelangle(self, axis):
        p_decelangle = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_DecelAngle(self.handler, axis, p_decelangle)
        value = p_decelangle.contents
        print(f"function_name->ret_val:{ret_val}, decelangle:{value}")
        return value

    def aux_direct_get_endmove(self, axis):
        p_endmove = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_EndMove(self.handler, axis, p_endmove)
        value = p_endmove.contents
        print(f"function_name->ret_val:{ret_val}, endmove:{value}")
        return value

    def aux_direct_get_endmovebuffer(self, axis):
        p_endmovebuffer = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_EndMoveBuffer(self.handler, axis, p_endmovebuffer)
        value = p_endmovebuffer.contents
        print(f"function_name->ret_val:{ret_val}, endmovebuffer:{value}")
        return value

    def aux_direct_get_endmovespeed(self, axis):
        p_endmovespeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_EndMoveSpeed(self.handler, axis, p_endmovespeed)
        value = p_endmovespeed.contents
        print(f"function_name->ret_val:{ret_val}, endmovespeed:{value}")
        return value

    def aux_direct_get_errormask(self, axis):
        p_errormask = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Errormask(self.handler, axis, p_errormask)
        value = p_errormask.contents
        print(f"function_name->ret_val:{ret_val}, errormask:{value}")
        return value

    def aux_direct_get_fastjog(self, axis):
        p_fastjog = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_FastJog(self.handler, axis, p_fastjog)
        value = p_fastjog.contents
        print(f"function_name->ret_val:{ret_val}, fastjog:{value}")
        return value

    def aux_direct_get_fastdec(self, axis):
        p_fastdec = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_FastDec(self.handler, axis, p_fastdec)
        value = p_fastdec.contents
        print(f"function_name->ret_val:{ret_val}, fastdec:{value}")
        return value

    def aux_direct_get_fe(self, axis):
        p_fe = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Fe(self.handler, axis, p_fe)
        value = p_fe.contents
        print(f"function_name->ret_val:{ret_val}, fe:{value}")
        return value

    def aux_direct_get_felimit(self, axis):
        p_felimit = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_FeLimit(self.handler, axis, p_felimit)
        value = p_felimit.contents
        print(f"function_name->ret_val:{ret_val}, felimit:{value}")
        return value

    def aux_direct_get_ferange(self, axis):
        p_ferange = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_FeRange(self.handler, axis, p_ferange)
        value = p_ferange.contents
        print(f"function_name->ret_val:{ret_val}, ferange:{value}")
        return value

    def aux_direct_get_fholdin(self, axis):
        p_fholdin = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_FholdIn(self.handler, axis, p_fholdin)
        value = p_fholdin.contents
        print(f"function_name->ret_val:{ret_val}, fholdin:{value}")
        return value

    def aux_direct_get_fhspeed(self, axis):
        p_fhspeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Fhspeed(self.handler, axis, p_fhspeed)
        value = p_fhspeed.contents
        print(f"function_name->ret_val:{ret_val}, fhspeed:{value}")
        return value

    def aux_direct_get_forcespeed(self, axis):
        p_forcespeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_ForceSpeed(self.handler, axis, p_forcespeed)
        value = p_forcespeed.contents
        print(f"function_name->ret_val:{ret_val}, forcespeed:{value}")
        return value

    def aux_direct_get_fslimit(self, axis):
        p_fslimit = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_FsLimit(self.handler, axis, p_fslimit)
        value = p_fslimit.contents
        print(f"function_name->ret_val:{ret_val}, fslimit:{value}")
        return value

    def aux_direct_get_fullspradius(self, axis):
        p_fullspradius = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_FullSpRadius(self.handler, axis, p_fullspradius)
        value = p_fullspradius.contents
        print(f"function_name->ret_val:{ret_val}, fullspradius:{value}")
        return value

    def aux_direct_get_fwdin(self, axis):
        p_fwdin = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_FwdIn(self.handler, axis, p_fwdin)
        value = p_fwdin.contents
        print(f"function_name->ret_val:{ret_val}, fwdin:{value}")
        return value

    def aux_direct_get_fwdjog(self, axis):
        p_fwdjog = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_FwdJog(self.handler, axis, p_fwdjog)
        value = p_fwdjog.contents
        print(f"function_name->ret_val:{ret_val}, fwdjog:{value}")
        return value

    def aux_direct_get_ifidle(self, axis):
        p_ifidle = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_IfIdle(self.handler, axis, p_ifidle)
        value = p_ifidle.contents
        print(f"function_name->ret_val:{ret_val}, ifidle:{value}")
        return value

    def aux_direct_get_invertstep(self, axis):
        p_invertstep = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_InvertStep(self.handler, axis, p_invertstep)
        value = p_invertstep.contents
        print(f"function_name->ret_val:{ret_val}, invertstep:{value}")
        return value

    def aux_direct_get_interpfactor(self, axis):
        p_interpfactor = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_InterpFactor(self.handler, axis, p_interpfactor)
        value = p_interpfactor.contents
        print(f"function_name->ret_val:{ret_val}, interpfactor:{value}")
        return value

    def aux_direct_get_jogspeed(self, axis):
        p_jogspeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_JogSpeed(self.handler, axis, p_jogspeed)
        value = p_jogspeed.contents
        print(f"function_name->ret_val:{ret_val}, jogspeed:{value}")
        return value

    def aux_direct_get_linkax(self, axis):
        p_linkax = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Linkax(self.handler, axis, p_linkax)
        value = p_linkax.contents
        print(f"function_name->ret_val:{ret_val}, linkax:{value}")
        return value

    def aux_direct_get_loaded(self, axis):
        p_loaded = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Loaded(self.handler, axis, p_loaded)
        value = p_loaded.contents
        print(f"function_name->ret_val:{ret_val}, loaded:{value}")
        return value

    def aux_direct_get_lspeed(self, axis):
        p_lspeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Lspeed(self.handler, axis, p_lspeed)
        value = p_lspeed.contents
        print(f"function_name->ret_val:{ret_val}, lspeed:{value}")
        return value

    def aux_direct_get_homewait(self, axis):
        p_homewait = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_HomeWait(self.handler, axis, p_homewait)
        value = p_homewait.contents
        print(f"function_name->ret_val:{ret_val}, homewait:{value}")
        return value

    def aux_direct_get_mark(self, axis):
        p_mark = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Mark(self.handler, axis, p_mark)
        value = p_mark.contents
        print(f"function_name->ret_val:{ret_val}, mark:{value}")
        return value

    def aux_direct_get_markb(self, axis):
        p_markb = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_MarkB(self.handler, axis, p_markb)
        value = p_markb.contents
        print(f"function_name->ret_val:{ret_val}, markb:{value}")
        return value

    def aux_direct_get_maxspeed(self, axis):
        p_maxspeed = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_MaxSpeed(self.handler, axis, p_maxspeed)
        value = p_maxspeed.contents
        print(f"function_name->ret_val:{ret_val}, maxspeed:{value}")
        return value

    def aux_direct_get_merge(self, axis):
        p_merge = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Merge(self.handler, axis, p_merge)
        value = p_merge.contents
        print(f"function_name->ret_val:{ret_val}, merge:{value}")
        return value

    def aux_direct_get_movesbuffered(self, axis):
        p_movesbuffered = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_MovesBuffered(self.handler, axis, p_movesbuffered)
        value = p_movesbuffered.contents
        print(f"function_name->ret_val:{ret_val}, movesbuffered:{value}")
        return value

    def aux_direct_get_movecurmark(self, axis):
        p_movecurmark = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_MoveCurmark(self.handler, axis, p_movecurmark)
        value = p_movecurmark.contents
        print(f"function_name->ret_val:{ret_val}, movecurmark:{value}")
        return value

    def aux_direct_get_mspeed(self, axis):
        p_mspeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Mspeed(self.handler, axis, p_mspeed)
        value = p_mspeed.contents
        print(f"function_name->ret_val:{ret_val}, mspeed:{value}")
        return value

    def aux_direct_get_mtype(self, axis):
        p_mtype = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Mtype(self.handler, axis, p_mtype)
        value = p_mtype.contents
        print(f"function_name->ret_val:{ret_val}, mtype:{value}")
        return value

    def aux_direct_get_offpos(self, axis):
        p_offpos = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Offpos(self.handler, axis, p_offpos)
        value = p_offpos.contents
        print(f"function_name->ret_val:{ret_val}, offpos:{value}")
        return value

    def aux_direct_get_openwin(self, axis):
        p_openwin = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_OpenWin(self.handler, axis, p_openwin)
        value = p_openwin.contents
        print(f"function_name->ret_val:{ret_val}, openwin:{value}")
        return value

    def aux_direct_get_regpos(self, axis):
        p_regpos = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_RegPos(self.handler, axis, p_regpos)
        value = p_regpos.contents
        print(f"function_name->ret_val:{ret_val}, regpos:{value}")
        return value

    def aux_direct_get_regposb(self, axis):
        p_regposb = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_RegPosB(self.handler, axis, p_regposb)
        value = p_regposb.contents
        print(f"function_name->ret_val:{ret_val}, regposb:{value}")
        return value

    def aux_direct_get_remain(self, axis):
        p_remain = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Remain(self.handler, axis, p_remain)
        value = p_remain.contents
        print(f"function_name->ret_val:{ret_val}, remain:{value}")
        return value

    def aux_direct_get_remain_buffer(self, axis):
        p_remain_buffer = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_Remain_Buffer(self.handler, axis, p_remain_buffer)
        value = p_remain_buffer.contents
        print(f"function_name->ret_val:{ret_val}, remain_buffer:{value}")
        return value

    def aux_direct_get_openrepdist(self, axis):
        p_openrepdist = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_OpenRepDist(self.handler, axis, p_openrepdist)
        value = p_openrepdist.contents
        print(f"function_name->ret_val:{ret_val}, openrepdist:{value}")
        return value

    def aux_direct_get_repoption(self, axis):
        p_repoption = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_RepOption(self.handler, axis, p_repoption)
        value = p_repoption.contents
        print(f"function_name->ret_val:{ret_val}, repoption:{value}")
        return value

    def aux_direct_get_revin(self, axis):
        p_revin = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_RevIn(self.handler, axis, p_revin)
        value = p_revin.contents
        print(f"function_name->ret_val:{ret_val}, revin:{value}")
        return value

    def aux_direct_get_revjog(self, axis):
        p_revjog = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_RevJog(self.handler, axis, p_revjog)
        value = p_revjog.contents
        print(f"function_name->ret_val:{ret_val}, revjog:{value}")
        return value

    def aux_direct_get_rslimit(self, axis):
        p_rslimit = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_RsLimit(self.handler, axis, p_rslimit)
        value = p_rslimit.contents
        print(f"function_name->ret_val:{ret_val}, rslimit:{value}")
        return value

    def aux_direct_get_sramp(self, axis):
        p_sramp = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Sramp(self.handler, axis, p_sramp)
        value = p_sramp.contents
        print(f"function_name->ret_val:{ret_val}, sramp:{value}")
        return value

    def aux_direct_get_startmovespeed(self, axis):
        p_startmovespeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_StartMoveSpeed(self.handler, axis, p_startmovespeed)
        value = p_startmovespeed.contents
        print(f"function_name->ret_val:{ret_val}, startmovespeed:{value}")
        return value

    def aux_direct_get_stopangle(self, axis):
        p_stopangle = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_StopAngle(self.handler, axis, p_stopangle)
        value = p_stopangle.contents
        print(f"function_name->ret_val:{ret_val}, stopangle:{value}")
        return value

    def aux_direct_get_vectorbuffered(self, axis):
        p_vectorbuffered = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_VectorBuffered(self.handler, axis, p_vectorbuffered)
        value = p_vectorbuffered.contents
        print(f"function_name->ret_val:{ret_val}, vectorbuffered:{value}")
        return value

    def aux_direct_get_vpspeed(self, axis):
        p_vpspeed = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_VpSpeed(self.handler, axis, p_vpspeed)
        value = p_vpspeed.contents
        print(f"function_name->ret_val:{ret_val}, vpspeed:{value}")
        return value

    def aux_direct_get_variablef(self, axis):
        p_variablef = ctypes.pointer(ctypes.c_float(0.0))
        ret_val = self.zaux_lib.Zaux_direct_get_Variablef(self.handler, axis, p_variablef)
        value = p_variablef.contents
        print(f"function_name->ret_val:{ret_val}, variablef:{value}")
        return value

    def aux_direct_get_variableint(self, axis):
        p_variableint = ctypes.pointer(ctypes.c_int(0))
        ret_val = self.zaux_lib.Zaux_direct_get_VariableInt(self.handler, axis, p_variableint)
        value = p_variableint.contents
        print(f"function_name->ret_val:{ret_val}, variableint:{value}")
        return value

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
