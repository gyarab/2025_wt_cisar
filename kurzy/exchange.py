import httpx

res = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

print("server odpovedel:", res.status_code)
lines = res.text.split('\n')
print("Kurzy pro den:", lines[0].split(" ")[0])

line_euro = ""
for line in lines:
    if "EUR" in line:
        line_euro = line
        break

if line_euro == "":
    print("Kurz EUR nebyl nalezen")
    exit(1)

rate_str = line_euro.split('|')[-1].replace(',' , '.')
rate = float(rate_str)

print("Kurz eura je", rate, "CZK")

while True:
    print("\nZvol typ převodu:")
    print("1 = EUR -> CZK")
    print("2 = CZK -> EUR")

    mode = input("Vyber si 1 nebo 2: ")

    if mode in ("1", "2"):
        break
    print("Neplatná volba!")

while True:
    try:
        amount = float(input("Zadej částku: ").replace(",", "."))
        if amount < 0:
            print("Částka musí byt kladná.")
            continue
        break
    except ValueError:
        print("Neplatné číslo!")

if mode == "1":
    result = amount * rate
    print(f"{amount:.2f} EUR = {result:.2f} CZK")
else:
    result = amount / rate
    print(f"{amount:.2f} CZK = {result:.2f} EUR")