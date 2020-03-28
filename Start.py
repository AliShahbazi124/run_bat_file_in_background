print("GitHub:https://github.com/AliShahbazi124")
bat = input("enter bat addres=>")
with open("finish.vbs","w") as file:
    file.write('Set WshShell = CreateObject("WScript.Shell")\n')
    file.write(f'WshShell.Run chr(34) & "{bat}" & Chr(34), 0\n')
    file.write('Set WshShell = Nothing')