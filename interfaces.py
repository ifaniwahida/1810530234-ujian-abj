ulang = "ya"

while ulang ==  "ya":
    pilih = input("Input data Trunk Interface baru [yes/no]?: ")
    if pilih == "yes":
        hostname = input("Masukkan Hostname Switch: ")
        hostname = input("Masukkan Nama Interface: ")
        file = open("db-interface.txt", 'a')
        file.write("\n" +interface)
    else:
        file = open("db-interface.txt", 'r')
        print(file.read())
        break;
    x = hostname[Hostname Switch]
    y = hostname[Interface]
    #print(x)
    if isinstance(x, str):
        print("hostname = "+ kelas +" ("+ x +")")
    else:
        print("Class IP = "+ kelas +" ("+ x['NetID'] +" bit NetID, " + x['HostID'] +" bit HostID)")