import ctypes

class ZmcLibUsing:
    def __init__(self):
        self.zaux_lib = None
        self.zmotion_lib = None
        self.zaux_lib = ctypes.cdll.LoadLibrary('./zmc/zauxdll.dll')
        self.zmotion_lib = ctypes.cdll.LoadLibrary('./zmc/zmotion.dll')

if __name__ == "__main__":
    test_obj = ZmcLibUsing()
    ##test_obj.zmotion_lib.ZMC_Open.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p]
    ##test_obj.zmotion_lib.ZMC_Open.restype = ctypes.c_int
    ret_val = test_obj.zmotion_lib.ZMC_Open(2, "127.0.0.1", ctypes.c_void_p())
    print(f"ret_val is:{ret_val}")

