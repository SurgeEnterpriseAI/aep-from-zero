"""Generate the Bloom sample data for AEP From Zero.

Everything here is synthetic: Bloom is a fictional brand, every person is made up, every email
ends in @example.com and every phone number uses the 555-01XX range kept for fiction.

Seeded, so every run writes byte-identical files. By default it rewrites the files that ship in
this folder:
  bloom-customers-500.csv    the 500-row trial customer file (dirty on purpose: casing, phone shapes,
                             duplicate emails)
  bloom-orders-500.csv       the 500-row trial order file, with the five deliberately broken rows
  bloom-identities-200.csv   identity links (ECID, email, BloomID) for 200 test customers, plus one
                             planted shared-tablet over-link
  bloom-customers-xdm.json   the 500 trial customers shaped as XDM JSON

With --full it also writes the full-size extract the trial files come from:
  bloom-customers.csv        10,000 customers
  bloom-orders.csv           25,000 orders (Priya's anchor order plus 24,999 more, five of them broken)

Usage: python generate_datasets.py [--full] [--out FOLDER]
"""
import argparse, csv, datetime, json, os, random

random.seed(20260818)
HERE = os.path.dirname(os.path.abspath(__file__))

FIRST = ["Priya","Aarav","Diya","Kabir","Anaya","Vivaan","Isha","Reyansh","Sara","Advait",
         "Maya","Arjun","Kiara","Ishaan","Riya","Aditya","Zara","Vihaan","Anika","Dhruv",
         "Emma","Liam","Olivia","Noah","Ava","Ethan","Sophia","Mason","Mia","Lucas",
         "Amelia","James","Harper","Benjamin","Ella","Henry","Grace","Leo","Chloe","Owen",
         "Wei","Mei","Chen","Ling","Hiro","Yuki","Sofia","Mateo","Lucia","Diego"]
LAST = ["Sharma","Patel","Reddy","Iyer","Nair","Kapoor","Rao","Menon","Gupta","Bose",
        "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Wilson","Moore",
        "Chen","Wang","Li","Zhang","Liu","Tanaka","Sato","Kim","Park","Nguyen"]
CITIES = [("Dallas","TX"),("Austin","TX"),("Houston","TX"),("Seattle","WA"),("Portland","OR"),
          ("Denver","CO"),("Chicago","IL"),("Boston","MA"),("Atlanta","GA"),("Miami","FL"),
          ("Phoenix","AZ"),("San Jose","CA"),("Newark","NJ"),("Columbus","OH"),("Raleigh","NC")]
# Product names follow Bloom's catalogue (bloom-product-catalogue.csv); prices are US dollars.
PRODUCTS = [
    ("BLM-SER-VITC-30","Vitamin C Serum 30 ml",34.00),
    ("BLM-MOIST-HYA-50","Hyaluronic Moisturiser 50 ml",20.00),
    ("BLM-CLN-GEL-150","Gentle Foaming Cleanser 150 ml",16.00),
    ("BLM-SUP-OMG3-60","Omega-3 Wellness Capsules 60 ct",28.00),
    ("BLM-SUP-MULTI-90","Daily Multivitamin 90 ct",22.00),
    ("BLM-SER-RET-30","Retinol Night Serum 30 ml",42.00),
    ("BLM-MSK-CLAY-100","Purifying Clay Mask 100 ml",24.00),
    ("BLM-SPF-MIN-50","Mineral Sunscreen SPF50 50 ml",26.00),
    ("BLM-SUP-COLL-30","Collagen Boost Sachets 30 ct",38.00),
    ("BLM-LIP-BALM-08","Repair Lip Balm 8 ml",9.00),
]
TIERS = ["Bronze","Silver","Gold"]
CUST_COLS = ["bloom_id","email","first_name","last_name","phone","loyalty_tier",
             "loyalty_points","join_date","city","state","country",
             "email_consent","sms_consent","push_consent"]

# Priya Sharma, the hero customer used throughout the course (matches the sample JSON files).
PRIYA = {
    "bloom_id":"BLM-CUST-004217","email":"priya.sharma@example.com",
    "first_name":"Priya","last_name":"Sharma","phone":"+1-469-555-0142",
    "loyalty_tier":"Gold","loyalty_points":"2340","join_date":"2023-11-02",
    "city":"Dallas","state":"TX","country":"US",
    "email_consent":"true","sms_consent":"false","push_consent":"true",
}
# Background customers the episodes name with an ID. Applied as each row is generated, so the
# random stream (and every other row) stays the same. BLM-CUST-000002 (Liam Iyer, Bronze, 259)
# already comes out of the generator as the course describes him.
NAMED = {
    "BLM-CUST-000048": {"first_name":"Maya","last_name":"Rao","email":"maya.rao48@example.com",
                        "loyalty_tier":"Silver","loyalty_points":"880"},
    "BLM-CUST-000101": {"first_name":"Noah","last_name":"Kim","email":"noah.kim101@example.com",
                        "loyalty_tier":"Gold","loyalty_points":"4120"},
    "BLM-CUST-000210": {"first_name":"Zara","last_name":"Bose","email":"zara.bose210@example.com",
                        "loyalty_tier":"Bronze","loyalty_points":"35"},
}
# The planted shared-tablet over-link (episode 7): two relatives in Dallas each signed in to the
# Bloom app on one family tablet, so one ECID is seen with two emails and two BloomIDs.
TABLET_ECID = "61833074552910846205"
TABLET_LINKS = [("BLM-CUST-000121","ella.davis121@example.com"),
                ("BLM-CUST-000144","olivia.davis144@example.com")]

# No join date may lie in the future. Dates after 30 June 2026 are squeezed, in order, into
# July to September 2026, so the newest join date is 29 September 2026.
PIVOT = datetime.date(2026, 6, 30)


def clamp_join(jd):
    d = datetime.date.fromisoformat(jd)
    if d <= PIVOT:
        return jd
    return (PIVOT + datetime.timedelta(days=((d - PIVOT).days + 1) // 2)).isoformat()


def phone_dirty(seed_n):
    """Return a fictional phone (555-01XX) in one of the five messy shapes Data Prep must normalise."""
    a, b, c = 200 + seed_n % 700, 555, 100 + seed_n % 100
    fmts = [
        f"+1-{a}-{b}-{c:04d}",
        f"({a}) {b}-{c:04d}",
        f"{a}.{b}.{c:04d}",
        f"{a}{b}{c:04d}",
        f"1-{a}-{b}-{c:04d}",
    ]
    return random.choice(fmts)


# ---------------------------------------------------------------- customers (10,000)
customers = [PRIYA]
for i in range(2, 10001):
    bid = f"BLM-CUST-{i:06d}"
    fn, ln = random.choice(FIRST), random.choice(LAST)
    # deliberate dirt: mixed-case emails, occasional duplicate email (2 rows share one address)
    base = f"{fn.lower()}.{ln.lower()}{i}@example.com"
    email = base
    if random.random() < 0.15:  # 15% have odd casing
        email = base.replace(fn.lower(), fn)  # e.g. Priya.sharma...
    if random.random() < 0.02 and customers:  # 2% duplicate an existing email (dedup lesson)
        email = random.choice(customers)["email"]
    tier = random.choices(TIERS, weights=[55, 30, 15])[0]
    pts = {"Bronze":random.randint(0,499),"Silver":random.randint(500,1499),
           "Gold":random.randint(1500,6000)}[tier]
    yr = random.choice([2021,2022,2023,2024,2025,2026])
    jd = f"{yr}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
    city, st = random.choice(CITIES)
    row = {
        "bloom_id":bid,"email":email,"first_name":fn,"last_name":ln,
        "phone":phone_dirty(i),"loyalty_tier":tier,"loyalty_points":str(pts),
        "join_date":clamp_join(jd),"city":city,"state":st,"country":"US",
        "email_consent":random.choice(["true","true","true","false"]),
        "sms_consent":random.choice(["true","false","false"]),
        "push_consent":random.choice(["true","false"]),
    }
    row.update(NAMED.get(bid, {}))
    customers.append(row)

# ---------------------------------------------------------------- orders (25,000, five broken)
# One product line per row; price is the line total. Priya's order BLM-88412 has two lines
# (54.00 in all, see sample-order-event.json); the order file carries its first line only.
ORDER_COLS = ["order_id","bloom_id","email","order_timestamp","sku","product_name",
              "quantity","price","currency","ship_city","ship_state"]
orders = [["BLM-88412","BLM-CUST-004217","priya.sharma@example.com",
           "2026-08-18T19:52:47Z","BLM-SER-VITC-30","Vitamin C Serum 30 ml",
           "1","34.00","USD","Dallas","TX"]]
# The five deliberately broken rows that episodes 5 and 6 teach, by position in the file.
broken_at = {4200:1, 9100:2, 14700:3, 19300:4, 23800:5}
for i in range(1, 25000):
    cust = random.choice(customers)
    sku, pname, price = random.choice(PRODUCTS)
    oid = f"BLM-{100000+i}"
    mon = random.randint(1,8); day = random.randint(1,28)
    hh, mm, ss = random.randint(0,23), random.randint(0,59), random.randint(0,59)
    ts = f"2026-{mon:02d}-{day:02d}T{hh:02d}:{mm:02d}:{ss:02d}Z"
    qty = random.choices([1,1,1,2,3], weights=[60,15,10,10,5])[0]
    row = [oid, cust["bloom_id"], cust["email"], ts, sku, pname,
           str(qty), f"{price*qty:.2f}", "USD", cust["city"], cust["state"]]
    kind = broken_at.get(i)
    if kind == 1:   row[3] = ""                   # empty order_timestamp
    elif kind == 2: row[3] = "2026/13/45 25:99"   # a date that cannot exist
    elif kind == 3: row[7] = "N/A"                # text where a price belongs
    elif kind == 4: row[1] = ""; row[2] = ""      # no bloom_id and no email
    elif kind == 5: row[7] = "-20.00"             # a valid number that makes no business sense
    orders.append(row)

# ---------------------------------------------------------------- identities (200 test customers)
identities = [["38472919862011456743","priya.sharma@example.com","BLM-CUST-004217"]]  # Priya's phone app
for c in customers[1:200]:
    ecid = "".join(str(random.randint(0,9)) for _ in range(20))
    identities.append([ecid, c["email"], c["bloom_id"]])
for bid, email in TABLET_LINKS:
    identities.append([TABLET_ECID, email, bid])

# ---------------------------------------------------------------- the 500-row trial draw
# The trial order file is one fixed draw from the full file: Priya's order, the five broken rows
# and 494 orders placed by the 500 trial customers, in this order. Keep it fixed: the episode 6
# numbers (497 ingested, 7 failed) come from this exact file.
TRIAL_ORDERS = """
    110327 122854 112928 115164 124043 113954 100500 115237 108570 114635 104923 105889
    104723 124502 110897 112413 103276 103409 108275 122008 124824 118020 101216 122690
    117165 107419 103099 117797 115502 101904 113740 115503 115678 116657 120081 111845
    108297 109674 111784 113168 117638 123780 115280 116083 112964 124251 115553 112944
    115268 103145 114395 111478 108034 124955 111316 119298 114009 117550 115877 113639
    121033 112102 115542 114820 124479 124032 124095 107011 119145 112091 103214 101504
    101992 123937 102677 124072 122197 106728 118235 121994 111530 111526 121170 105277
    115535 119766 100626 118848 115845 122137 107694 115032 109140 101244 119058 107229
    102082 109424 100090 102107 101201 106012 116796 110748 120224 103213 122569 100041
    100171 109881 116978 109619 106459 119784 116399 109135 123888 122114 101826 110942
    104065 100392 109981 121056 115329 108028 106964 104827 117511 107929 104061 101355
    119589 122139 106309 104989 111426 107161 102501 124579 106849 114704 104616 114398
    103456 114738 106285 112613 117190 114983 122528 116167 100288 118921 106457 106103
    114297 106358 122207 113876 116542 116205 124305 106421 104912 121912 118487 114700
    117204 119828 122827 100751 120864 104750 100844 100568 115338 113139 121416 117799
    121083 107008 110862 112914 115750 122535 119883 109891 106208 104655 101020 102311
    118745 105786 107324 123999 113605 116926 106914 124747 115688 110017 124886 124618
    115306 100462 112283 107426 115568 120453 112317 107674 119024 110754 109576 122124
    101258 112174 118207 109951 115854 107960 103685 121014 118946 100683 114991 113069
    123982 114644 112639 104416 108875 112087 114714 120145 100385 122726 121270 112820
    102670 118547 116330 107431 123297 118413 109396 107809 111002 106353 116905 107491
    117075 123261 116633 111247 108642 114861 118957 111648 115722 106884 107233 116566
    103704 110814 101511 120856 108816 109608 120974 118520 106465 124408 104469 114712
    114170 113423 111664 106382 107086 121436 110812 101021 120181 117177 112467 104080
    122846 102270 116689 117935 103758 120606 124825 113802 106922 88412 118876 123789
    108067 108071 121537 111891 120816 108422 118258 124084 112359 123431 117618 116610
    119156 111604 106595 116646 107415 105860 108479 101228 100408 115319 107823 110540
    111840 106905 100853 103678 114101 100593 118781 119851 117739 121597 113887 114307
    122140 108802 122590 107580 110881 100253 103536 103959 113573 107028 109824 112907
    115628 107932 107144 110555 117955 109538 113392 106392 115026 121826 102964 105578
    119769 109255 122487 113877 122130 104200 112018 114554 103662 111560 104710 109603
    116745 115920 114290 114420 104128 110619 124513 100249 121993 108610 114058 104758
    122992 121747 103831 116188 102190 116811 108073 117700 115891 109361 121144 111349
    112203 119300 123249 124083 101942 114342 111377 105348 119216 105776 112267 106046
    120380 120766 124801 110669 119943 114964 119225 108675 112121 101379 102535 121819
    113001 107217 123723 105273 115991 105104 118115 106792 101961 104007 105707 104385
    119752 121238 111869 121546 121380 103517 121157 108448 115715 101758 108577 106901
    106991 100547 120322 110045 117184 111741 109100 103617 117217 108553 115643 119031
    101384 124300 117039 104478 100111 107778 102149 106005 123800 106879 117981 102154
    104140 122228 100120 108018 114218 106689 117333 103943 117111 100488 111054 104455
    111504 121262 122062 118805 122393 116715 114905 116659 109682 113404 112699 120722
    108174 112583 117450 100092 117267 107559 118343 112621
""".split()


def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def xdm(c):
    return {"personalEmail": {"address": c["email"]},
            "person": {"name": {"firstName": c["first_name"], "lastName": c["last_name"]}},
            "homeAddress": {"city": c["city"], "stateProvince": c["state"], "countryCode": "US"},
            "mobilePhone": {"number": c["phone"]}}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--full", action="store_true", help="also write the 10,000-customer and 25,000-order files")
    ap.add_argument("--out", default=HERE, help="folder to write into (default: this script's folder)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    by_id = {r[0]: r for r in orders}
    trial = customers[:500]
    write_csv(os.path.join(a.out, "bloom-customers-500.csv"), CUST_COLS, [[c[k] for k in CUST_COLS] for c in trial])
    write_csv(os.path.join(a.out, "bloom-orders-500.csv"), ORDER_COLS, [by_id[f"BLM-{n}"] for n in TRIAL_ORDERS])
    write_csv(os.path.join(a.out, "bloom-identities-200.csv"), ["ecid","email","bloom_id"], identities)
    with open(os.path.join(a.out, "bloom-customers-xdm.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps([xdm(c) for c in trial]))
    if a.full:
        write_csv(os.path.join(a.out, "bloom-customers.csv"), CUST_COLS, [[c[k] for k in CUST_COLS] for c in customers])
        write_csv(os.path.join(a.out, "bloom-orders.csv"), ORDER_COLS, orders)
    print("trial files: 500 customers, 500 orders (five broken), 202 identity links (200 customers + the tablet)")
    if a.full:
        print("full files: %d customers, %d orders" % (len(customers), len(orders)))
    print("written to", a.out)


if __name__ == "__main__":
    main()
