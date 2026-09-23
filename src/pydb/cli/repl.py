def main():
    
    while True:
        cmd = input("pydb> ")
        
        if cmd.startswith('.'): # Recognized META_COMMAND
            
           if cmd == ".exit":
               break
           else:
               meta_command_handler(cmd) 
        else:
            # TODO
            # sql_parse(cmd)
            pass

def meta_command_handler(cmd: str):
    
    if cmd == ".help":
        a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
        print(a)
    else:
        print("Unrecognized command.")