import re

def extract_function_names_and_declarations_from_header(header_file):
    with open(header_file, 'r') as f:
        content = f.read()
        function_pattern = r'int32\s+__stdcall\s+\**(\w+)\s*\((.*?)\)'
        functions = re.findall(function_pattern, content)
        return functions

if __name__ == "__main__":
    header_file = "zauxdll.h"
    function_names = extract_function_names_and_declarations_from_header(header_file)
    print("Function names in header file:")
    for func_name, parameters in function_names:
        if func_name.startswith("ZAux_Direct_Set"):
            if len(str(parameters).split(",")) == 3:
                type_name = (str(parameters).split(",")[-1]).split(" ")[1]
                function_name = func_name.lower()[1:]
                api_name = function_name
                print (f'''
                    def {function_name}(self, axis, location):
                        ret_val = self.zaux_lib.{func_name}(self.handler, axis, ctypes.c_{type_name}(location))
                        print(f"{function_name}->ret_val:{"ret_val"}")
                        ''')
        if func_name.startswith("ZAux_Direct_Get"):
            if len(str(parameters).split(",")) == 3:
                type_name = (str(parameters).split(",")[-1]).split(" ")[1]
                function_name = func_name.lower()[1:]
                api_name = function_name
                var_name = str(function_name).split("get")[1]
                if type_name == "float":
                    print(f'''
                            def {function_name}(self, axis):
                                p_{var_name} = ctypes.pointer(ctypes.c_float(0.0))
                                ret_val = self.zaux_lib.{func_name}(self.handler, axis, p_{var_name})
                                value = p_{var_name}.contents
                                print(f"function_name->ret_val:ret_val, {var_name}:value")
                                return value
                            ''')
                if type_name == "int":
                    print(f'''
                            def {function_name}(self, axis):
                                p_{var_name} = ctypes.pointer(ctypes.c_int(0))
                                ret_val = self.zaux_lib.{func_name}(self.handler, axis, p_{var_name})
                                value = p_{var_name}.contents
                                print(f"function_name->ret_val:ret_val, {var_name}:value")
                                return value
                            ''')