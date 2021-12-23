from colors import *
from main import *

blue("[!] Enter the details for attack [!]")
print()
print("[-] Website :",end=" ")
url=input()
yellow("[?] Checking the validity of URL [?]")
print()
try:
    res = requests.get(url)
    if res.status_code==200:
        green("[#] valid url provided [#]")

        urls.append(url)
        print("[-] Depth :",end=" ")
        n=int(input())
        green(f'[#] Depth selected as {n} [#] ' )
        print()
        print("[-] Output File Name :",end=" ")
        o=input()

        depth(n)
        with open(f'{o}.txt',"a") as f:
            f.write(f"Gathered {urls.__len__()} urls\n")
            for u in urls:
                f.write(f'{u}\n')
except Exception as e:
    red("invalid url")
