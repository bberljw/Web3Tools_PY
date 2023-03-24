from web3.auto import w3
from concurrent.futures import ThreadPoolExecutor
import threading
import sys

# 用于控制所有线程退出的锁
lock = threading.Lock()
# 标志位，用于表示是否已经找到匹配的地址
found_flag = False

def generate_eth_address(suffix):
    account = w3.eth.account.create()
    address = account.address
    private_key = account.privateKey.hex()

    if address.endswith(suffix):
        return private_key, address

    return None

def generate_addresses(num_threads, suffix, file_path):
    found_flag = False
    while not found_flag:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(generate_eth_address, suffix) for _ in range(num_threads)]
            for future in futures:
                result = future.result()
                if result is not None:
                    private_key, address = result

                    # 将私钥和地址写入文件
                    with open(file_path, 'a') as f:
                        f.write(f"{address}, {private_key}\n")

                    if address.endswith(suffix):
                        found_flag = True
                        break

        if not found_flag:
            print("没有找到匹配的地址")

def main():
    num_threads = 200  # 线程数
    suffix = "000000"  # 自定义尾号
    file_path = "eth_addresses.txt"  # 文件路径
    
    generate_addresses(num_threads, suffix, file_path)

if __name__ == "__main__":
    main()
