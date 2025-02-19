import pexpect

def read_gok_sensor(mac):
    """Liest die Sensordaten über BLE"""
    try:
        # Aktivieren der Benachrichtigungen
        child = pexpect.spawn(f"gatttool -t random -b {mac} --char-write-req --handle=0x000f --value=0100")
        child.expect("Characteristic value was written successfully", timeout=3)
        child.sendline("disconnect")
        child.sendline("exit")

        # Verbindung neu aufbauen
        child = pexpect.spawn(f"gatttool -I -t random -b {mac}")
        for _ in range(5):
            child.sendline("connect")
            try:
                child.expect("Connection successful", timeout=3)
                break
            except pexpect.TIMEOUT:
                continue
        else:
            return {"error": "Connection timeout"}

        # Daten abrufen
        child.sendline("char-read-uuid 00007082-a20b-4d4d-a4de-7f071dbbc1d8")
        child.expect("handle: 0x000e \t value: ", timeout=5)
        child.expect("\r\n", timeout=0)
        raw_data = child.before.strip().decode("utf-8")

        # Verbindung trennen
        child.sendline("disconnect")
        child.sendline("exit")

        # Hex-Daten in Werte umwandeln
        hex_values = raw_data.split()
        percentage = int(hex_values[0], 16)  
        voltage = int(hex_values[1], 16) / 1000  

        return {
            "gas_level": percentage,
            "voltage": voltage
        }

    except Exception as e:
        return {"error": str(e)}
